from .models import NFT
from .serializers import NFTSerializer
from rest_framework import viewsets

class NFTView(viewsets.ModelViewSet):
    queryset = NFT.objects.all()
    serializer_class = NFTSerializer

    
    

        




