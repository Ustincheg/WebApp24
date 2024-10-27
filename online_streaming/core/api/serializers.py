from rest_framework import serializers

from ..models import Films


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = ('id', 'title', 'kinopoisk_id')


class SubjectSerializer_Detail(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = '__all__'