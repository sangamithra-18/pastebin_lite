from django.db import models

import uuid
from django.utils import timezone
from datetime import timedelta

class Pastebin_content(models.Model):
   
   EXPIRY_CHOICES = [
        ("burn", "Burn after read"),
        ("1_hour", "1 Hour"),
        ("1_day", "1 Day"),
        ("1_week", "1 Week"),
        ("2_weeks", "2 Weeks"),
        ("1_month", "1 Month"),
        ("6_months", "6 Months"),
        ("1_year", "1 Year"),
        ("never", "Never"),
    ]

   CATEGORY_CHOICES = [
        ("text", "Text"),
        ("code", "Code"),
        ("notes", "Notes"),
        ("secret", "Secret"),
        ("food",   "Food"),
        ("movies",  "Movies"),
        ("other",   "Other"),
    ]
   id=models.UUIDField( primary_key=True,
        default=uuid.uuid4,
        editable=False)
   
   content_paste=models.TextField()
   category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="none"
    )
   expiry = models.CharField(
        max_length=20,
        choices=EXPIRY_CHOICES,
        default="1 Hour"
    )

   created_at=models.DateTimeField(auto_now_add=True)
   expires_at=models.DateTimeField(null=True,blank=True)

   max_views=models.PositiveBigIntegerField(null=True,blank=True)
   views_count=models.PositiveBigIntegerField(default=0)

   is_active = models.BooleanField(default=True)

   def is_expired(self):
        """Check if paste is expired by time or views"""
        if self.expires_at and timezone.now() > self.expires_at:
            return True

        if self.max_views is not None and self.views_count >= self.max_views:
            return True

        return False

   def __str__(self):
        return f"Paste {self.id}"
   # Create your models here.
