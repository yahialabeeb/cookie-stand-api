from django.db.models.query import QuerySet
from rest_framework import generics, serializers
from .models import CookieStand
from .serializers import CookieSerialize
from .permissions import IsOwnerOrReader

# Create your views here.
class CookiesList(generics.ListCreateAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = CookieSerialize

class CookiesDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = CookieSerialize
    permission_classes = (IsOwnerOrReader,)