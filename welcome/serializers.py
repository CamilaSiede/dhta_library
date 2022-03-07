from rest_framework import serializers
from welcome.models import Books

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['title', 'author','description']