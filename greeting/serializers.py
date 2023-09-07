from rest_framework import serializers


class GreetSerializer(serializers.Serializer):
    greeting = serializers.CharField()
