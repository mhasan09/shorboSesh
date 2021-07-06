from rest_framework import serializers
from shorboSeshApp.models import NEWS


class NEWS_SERIALIZERS(serializers.ModelSerializer):
    class Meta:
        model = NEWS
        fields = ['id', 'NEWS_TITLE', 'NEWS_SUBTITLE', 'NEWS_LINK', 'NEWS_SOURCE', 'POST_CREATED_AT']
