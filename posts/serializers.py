from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    # postuser=serializers.ReadOnlyField(source='post_activities')
    # postattributes=serializers.ReadOnlyField(source='post_attributes')
    # category_name=serializers.ReadOnlyField(source='post_category_name')
    class Meta:
        model = Post
        fields ='__all__'
