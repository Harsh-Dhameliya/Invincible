from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class Customer(models.Model):
    customer_name = models.CharField(max_length=20, default=None)
    customer_email = models.EmailField(unique=True, default=None)
    customer_mobile = models.CharField(max_length=10, default=None)
    password = models.CharField(max_length=128)  # Ensure it's large enough for hashed passwords

    def set_password(self, raw_password):
        """Encrypt and set the password."""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Check if the password matches the hash."""
        return check_password(raw_password, self.password)
    
    def save(self, *args, **kwargs):
        """Ensure the password is always hashed before saving."""
        if not self.password.startswith('pbkdf2_sha256$'):  # Avoid rehashing an already hashed password
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.customer_name

    class Meta:
        db_table = 'customer'


