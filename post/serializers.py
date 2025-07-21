from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'context', 'created_at']

    def get_created_at(self, obj):
        return obj.created_at.strftime("%Y년 %m월 %d일")
