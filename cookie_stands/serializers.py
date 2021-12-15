from rest_framework import serializers
from .models import CookieStand

class CookieSerialize(serializers.ModelSerializer):
    class Meta:
        model = CookieStand
        field = "__all__"
