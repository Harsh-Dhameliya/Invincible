function validateData(data) {

 var status = true;

  if (data.name === "cname" || data.id =="r-form") {
    let name = document.getElementById("cname");
    const namePattern = /\d/;
  
    if (name.value.length > 0 && !namePattern.test(name.value) && name.value.length <= 20 && !/[!@#$%^&*(),.?":{}|<>]/.test(name.value)) {
      name.classList.remove("is-invalid");
      name.classList.add("is-valid");
    } else {
      name.classList.remove("is-valid");
      name.classList.add("is-invalid");
      status = false;
    }
  }
  if (data.name === "mobile" || data.id === "r-form") {
    const mobilePattern = /^[6-9]\d{9}$/;
    let mobile = document.getElementById("mobile");

      if (mobile.value.length >= 0 && mobilePattern.test(mobile.value)) {
        mobile.classList.remove("is-invalid");
        mobile.classList.add("is-valid");
      } else {
        mobile.classList.remove("is-valid");
        mobile.classList.add("is-invalid");
        status = false;
      }

  }
  if (data.name === "email" || data.id === "r-form") {

    const emailPattern = /^[a-z]*[0-9]*\@[a-z]*\.[a-z]*$/;
    let email = document.getElementById("email");

      if (email.value.length >= 0 && emailPattern.test(email.value)) {
        email.classList.remove("is-invalid");
        email.classList.add("is-valid");
      } else {
        email.classList.remove("is-valid");
        email.classList.add("is-invalid");
        status = false;
      }

  }
if (data.name === "password" || data.id === "r-form") {
    
    let password = document.getElementById("password");
    let passError = document.getElementById("pass-error")
    const passwordPattern = /[A-Z]/.test(password.value) && /\d/.test(password.value) && /[!@#$%^&*(),.?":{}|<>]/.test(password.value);


      if (password.value.length >= 8 && password.value.length <= 12  && passwordPattern ) 
        {
        passError.innerHTML = ""
        password.classList.remove("is-invalid");
        password.classList.add("is-valid");

      } else {
        password.classList.remove("is-valid");
        password.classList.add("is-invalid");
        if (data.name === "password") {
          passError.innerHTML = "Passord Should be contain A-Z,0-9,Special-character and length of password 8-12"
        }
        status = false;
      }

  }

if (data.name === "cpassword" || data.id === "r-form") {
    
    let cpassword = document.getElementById("cpassword");
    let password = document.getElementById("password");
    let cpassError = document.getElementById("cpass-error")



      if (cpassword.value === password.value && cpassword.value.length > 0) 
        {
        cpassError.innerHTML = ""
        cpassword.classList.remove("is-invalid");
        cpassword.classList.add("is-valid");

      } else {
        cpassword.classList.remove("is-valid");
        cpassword.classList.add("is-invalid");
        if (data.name === "cpassword") {
          
          cpassError.innerHTML = "Enter same password"
        }
        status = false;
      }

  }
  if (status == true) {

    return true;
  } else {
    return false;
  }

}


