from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    # postuser=serializers.ReadOnlyField(source='post_activities')
    # postattributes=serializers.ReadOnlyField(source='post_attributes')
    # category_name=serializers.ReadOnlyField(source='post_category_name')
    class Meta:
        model = Category
        fields ='__all__'
