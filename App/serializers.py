from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    username = serializers.EmailField()
    password = serializers.CharField()
    #email = serializers.EmailField()
    #content = serializers.CharField(max_length=200)
    #created = serializers.DateTimeField()

    