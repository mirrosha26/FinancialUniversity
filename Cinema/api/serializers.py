from rest_framework import serializers
from movies.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'movie', 'client', 'rental_start_date', 'rental_end_date', 'rental_cost']