from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
import uuid

class Collection(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True, blank=True)    
    creator_network = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
            return self.name

class NFT(models.Model):
    asset_id = models.UUIDField(max_length=30,default=uuid.uuid4, primary_key=True, editable=False, validators=[MinLengthValidator(16)])
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    picture = models.ImageField(null=True, blank=True)
    external_link = models.URLField(null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)    
    supply = models.CharField(max_length=255, null=True, blank=True)
    royalties = models.CharField(max_length=255, null=True, blank=True)    
    buyer = models.CharField(max_length=255, null=True, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.name