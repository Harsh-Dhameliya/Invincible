"""
URL configuration for Invincible project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import view
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Invincible Admin Panel" 
admin.site.site_title = "Invincible Admin Portal"
admin.site.index_title = "Invincible"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.Home ,name="home"),
    path('about-us/',view.AboutUs),
    path('events/',view.Packages),
    path('contact-us/',view.ContactUS),
    path('faq/',view.Faq),
    path('booking/<eslug>',view.Booking),
    path('description/<eslug>',view.Description),
    path('forgot-password/',view.Forgotpass),
    path('log-in/',view.Login,name="login"),
    path('log-out/',view.Logout,name="logout"),
    path('registration/',view.Registration , name="register"),
    path('otp-verify/',view.OTP ,name="verify_otp"),
    path('booking-receipt/',view.Receipt, name ="receipt"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
