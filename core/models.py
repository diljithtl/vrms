from django.db import models
from django.contrib.auth.models import User

# -------------------------
# Role Profile
# -------------------------
class Profile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('customer', 'Customer'),
        ('driver', 'Driver'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# -------------------------
# Vehicle
# -------------------------
class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=50)
    price_per_day = models.FloatField()

    status_choices = (
        ('available', 'Available'),
        ('booked', 'Booked'),
        ('unavailable', 'Unavailable')
    )
    status = models.CharField(max_length=20, choices=status_choices, default='available')

    def __str__(self):
        return self.name


# -------------------------
# Driver
# -------------------------
class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_no = models.CharField(max_length=50)

    status_choices = (
        ('available', 'Available'),
        ('ontrip', 'On Trip'),
        ('inactive', 'Inactive')
    )
    status = models.CharField(max_length=20, choices=status_choices, default='available')

    def __str__(self):
        return self.user.username


# -------------------------
# Booking
# -------------------------
class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)

    start_date = models.DateField()
    end_date = models.DateField()
    total_amount = models.FloatField()

    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"{self.customer} - {self.vehicle}"


# -------------------------
# Payment
# -------------------------
class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    method = models.CharField(max_length=20)
    paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(auto_now_add=True)
