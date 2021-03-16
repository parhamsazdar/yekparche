from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField, StringRelatedField

from seminar.models import *


class FileSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = File
        fields = ["file_name", "file", "user"]


class SeminarCustomerCome(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField()
    last_name = serializers.ReadOnlyField()
    phone = serializers.ReadOnlyField()

    class Meta:
        model = SeminarCustomer
        fields = ["first_name", "last_name", "phone", "come"]


class SeminarAllcustomer(PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
       model=SeminarCustomer


class SeprateCustomer(serializers.ModelSerializer):
    customer = SeminarAllcustomer(many=True,queryset=SeminarCustomer.objects.all())

    class Meta:
        model = User
        fields = ["username",'customer']
