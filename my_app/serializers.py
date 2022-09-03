from rest_framework import serializers
from .models import Category, Item


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate(self, value):
        if '!@#$%^&*' in value:
            raise serializers.ValidationError('Category could not contain "!@#$%^&*"')
        return value


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    def validate(self, data):
        if data['QR'] is None:
            raise serializers.ValidationError('category_id, price, item_id should be in QR')
        return f"{data['category_id']}C{data['price']}P{data['id']})"
