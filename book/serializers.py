from rest_framework import serializers
from book.models import *




class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(write_only=True)

    class Meta:
        model = Book

        fields = '__all__'


class JournalSerializer(serializers.ModelSerializer):
    title = serializers.CharField(write_only=True)

    class Meta:
        model = Journal

        fields = '__all__'


