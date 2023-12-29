from rest_framework import serializers

from .models import AdvantageItem, HeaderLink

class AdvantageItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdvantageItem
        fields = ('first_text', 'main_text', 'second_text', 'position')

class HeaderLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HeaderLink
        fields = ('endpoint', 'text')