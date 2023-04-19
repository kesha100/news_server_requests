from rest_framework import serializers


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField(default='')
    url = serializers.URLField()