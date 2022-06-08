from django.contrib.auth.models import User
from rest_framework import serializers

from backend.crm.models import Customer, Employee


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
        )
        ref_name = 'Custom User Serializer'


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'
        depth = 1


class EmployeeCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ('user', 'occupation', 'rg', 'cpf', 'active')

    def create(self, validated_data):
        # Cria user
        if 'user' in validated_data:
            user = validated_data.pop('user')

            user = User.objects.create(**user)
            employee = Employee.objects.create(user=user, **validated_data)

        return employee


class EmployeeUpdateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ('user', 'occupation', 'rg', 'cpf', 'active')

    def update(self, instance, validated_data):
        # Edita user
        if 'user' in validated_data:
            user = validated_data.pop('user')

            for attr, value in user.items():
                setattr(instance.user, attr, value)

            instance.user.save()

        # Edita demais campos
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance
