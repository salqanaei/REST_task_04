from rest_framework import serializers

from .models import Flight, Booking

from django.contrib.auth.models import User


class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ['destination', 'time', 'price', 'id']


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'id']


class BookingDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'passengers', 'id']


class UpdateBookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['date', 'passengers']

class CreateUserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'password', 'last_name', 'first_name']

	def create(self, validated_data):
		u = validated_data['username']
		password = validated_data['password']
		l = validated_data['last_name']
		f = validated_data['first_name']
		user = User(username = u, last_name = l, first_name = f)
		user.set_password(password)
		user.save()
		return validated_data

