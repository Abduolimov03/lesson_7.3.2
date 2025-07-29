from rest_framework import serializers
from .views import Macbook

class MacbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Macbook
        fields = '__all__'