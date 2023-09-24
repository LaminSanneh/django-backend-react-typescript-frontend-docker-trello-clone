from django.db.models import fields
from rest_framework import serializers

from .models import Board

class BoardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"
