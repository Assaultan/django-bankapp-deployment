from basicapp.models import Customers,Transfers
from rest_framework import serializers

class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    email = serializers.EmailField()
    balance = serializers.IntegerField()
    
    def create(self,validated_data):
        return Customers.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.email = validated_data.get('email',instance.email)
        instance.balance = validated_data.get('balance',instance.balance)
        instance.save()
        return instance