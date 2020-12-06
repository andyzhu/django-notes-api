from rest_framework import serializers 
from .models import Note

class NoteSerailizer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'content', 'created', 'updated')
        model = Note

