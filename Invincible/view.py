from django.shortcuts import render,redirect
from review.models import Review
from customer.models import Customer
from category.models import Category
from package.models import Package,Schedule
from booking.models import Bookings
import random
import smtplib 
from email.message import EmailMessage
from django.contrib.auth import authenticate 
from django.contrib.auth import login
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def Home(request):
    review = Review.objects.all()
    alldata = {"allreview" : review}
    # expiry_time = request.session.get_expiry_age()
    # print(expiry_time)
    print(review)
    if 'customer_id' in request.session:
        print("user loged in")
    return render(request,"index.html",alldata)

def AboutUs(request):
    return render(request,"about.html")

def Packages(request):
    
    package = Package.objects.all()
    # query = """SELECT category_category.id, category_category.category_name 
    # FROM category_category  
    # INNER JOIN package_package ON category_category.id = package_package.category_id;"""
    # category = Category.objects.raw(query)

    category_ids = package.values_list('category_id', flat=True).distinct()
    categories = Category.objects.filter(id__in=category_ids)
    
    # print(category)

    alldata = {"allpackage":package , "allcategory" : categories}              
    return render(request,"packages.html",alldata)                                                                    

def ContactUS(request):
    return render(request,"contact.html")

def Faq(request):
    return render(request,"faq.html")

def Description(request,eslug):
    if (request.method == 'POST'):
        name = request.POST["r-name"]
        review = request.POST["review"]
        newReview = Review(name = name , review = review)
        newReview.save()

    descriptiondata = Package.objects.get(Slug = eslug)
    schedule = Schedule.objects.all()
    data = {"alldata":descriptiondata,"allschedule":schedule}
    return render(request,"description.html",data)

def Forgotpass(request):
    return render(request,"forgotpwd.html")


def Registration(request):

    if request.method == 'POST':
        cname = request.POST["cname"]
        mobile = request.POST["mobile"]
        raw_password = request.POST["password"]
        email = request.POST["email"]

        # Check if the email is already registered
        if Customer.objects.filter(customer_email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect('register')


        otp = generate_otp()
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("harshdhameliya018@gmail.com", "twvc famp dvwj slzc")
        msg = EmailMessage()
        msg["Subject"] = "OTP Verification"
        msg["From"] = "harshdhameliya018@gmail.com"
        msg["To"] = email
        msg.set_content("""Dear {},

    Welcome to Invisible Tours and Travels! We are excited to have you onboard as you explore your next unforgettable journey with us.

    To complete your registration, please verify your email address. Use the One-Time Password (OTP) below to proceed:

    **Your OTP:** {}

    Please note, this OTP is valid for the next **10 minutes**. If you did not request this, please ignore this email.

    Thank you for choosing Invisible Tours and Travels. Let’s create unforgettable memories together!

    **Warm regards,**  
    The Invisible Team
    """.format(cname, otp)
)

        server.send_message(msg)

        # Save temporary data in session
        request.session['temp_data'] = {
            'cname': cname,
            'mobile': mobile,
            'email': email,
            'password': raw_password,
            'otp': otp
        }   
        request.session.set_expiry(600)

        return redirect('verify_otp')
    return render(request, "registration.html")

def OTP(request):
    if request.method == 'POST':
        u_otp = request.POST["otp"]
        temp_data = request.session.get('temp_data', {})

        if not temp_data:
            messages.error(request, "Session expired. Please try registering again.")
            return redirect('register')

        # Compare user OTP with generated OTP
        if u_otp == temp_data.get('otp'):
            # Create a new customer
            new_customer = Customer(
                customer_name=temp_data['cname'],
                customer_email=temp_data['email'],
                customer_mobile=temp_data['mobile']
            )
            new_customer.set_password(temp_data['password'])  # Encrypt the password
            new_customer.save()

            messages.success(request, "Account created successfully!")
            return redirect('login')
        else:
            messages.error(request, "Invalid OTP.")
            return redirect('verify_otp')

    return render(request, "otp-verify.html")

def Login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        raw_password = request.POST["password"]

        try:
            customer = Customer.objects.get(customer_email=email)
        except Customer.DoesNotExist:
            messages.error(request, "Invalid email or password!")
            return redirect('login')

        # Verify the password
        if customer.check_password(raw_password):
            # Login the user (using Django sessions)
            request.session['customer_id'] = customer.id
            messages.success(request, "Logged in successfully!")
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password!")

    return render(request, "login.html")

def Logout(request):
    if 'customer_id' in request.session:
        print("user log-out")
        del request.session['customer_id']  # Remove customer ID from session
    messages.success(request, "Logged out successfully!")
    return redirect('login')


def Booking(request,eslug,):

    if 'customer_id' not in request.session:  # ✅ Check if user is logged in
        messages.error(request, "You must log in first!")
        return redirect('login')
    
    customer_id = request.session["customer_id"]

    package  = Package.objects.get(Slug = eslug)
   
    
    package_name = {"packagedata":package}

    total = int( request.POST.get("total", 0))  # Get total, default to 0 if not found
    request.session['totaldata'] = {
    'total': total,
    'package_id': package.id  # Store only the package ID
}
    
    
    if request.method == 'POST':
        if total > 0:
            fnames = request.POST.getlist("fname")
            lnames = request.POST.getlist("lname")
            mobiles = request.POST.getlist("mobile")
            dobs = request.POST.getlist("date")
            genders = request.POST.getlist("gender")

            for x in range(total):  
                name = f"{fnames[x]} {lnames[x]}"
                mobile = mobiles[x]
                dob = dobs[x]
                gender = genders[x]
                bookingdata = Bookings(customer_id=customer_id, name=name,mobile_no=mobile, birth_date=dob, gender=gender)
                bookingdata.save()

        return redirect("receipt")

    return render(request,"booking.html",package_name)

def Receipt(request):
  

   totaldata = request.session.get('totaldata', {})
   tperson = totaldata.get('total', 1)


   package_id = totaldata.get('package_id')  # Retrieve package ID
   package = None
   if package_id:
       package = Package.objects.get(id=package_id)  # Fetch the package
       pack_price  = package.Package_price

       totalamount = int(tperson) * int(pack_price)

   
  
   
   query = f''' SELECT * FROM booking_bookings WHERE id > (SELECT MAX(id) - {tperson} FROM booking_bookings) ORDER BY id ASC;'''
   receipt = Bookings.objects.raw(query)

   data = {
        "receiptdata": receipt,
        "packages":package,
        "total":tperson,  # Passing session data as requested
        "totalprice":totalamount
    }
   return render(request,"receipt.html",data)  

def generate_otp(length=6):
    otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    return otp



############################################# notes #############################################

# note 1 : select category_name from  package_package A  inner join category_category B on a.category_id =  b.id;