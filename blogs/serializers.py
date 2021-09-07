from .models import Blog
from rest_framework import serializers

## Create a Serializer for Our Model
class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        # which fields should be serialized
        fields = ["id", "title", "body"]


