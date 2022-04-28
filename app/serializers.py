from .models import NFT
from rest_framework import serializers

class NFTSerializer(serializers.ModelSerializer):

    class Meta:
        model = NFT
        fields = '__all__'