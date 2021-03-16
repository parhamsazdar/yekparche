from api.permissions import IsSuperuserOrOwner
from seminar.serializers import *
from rest_framework import permissions
from rest_framework import generics


class FileCreate(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializers

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SeminarCustomerCome(generics.RetrieveUpdateAPIView):
    queryset = SeminarCustomer.objects.all()
    serializer_class = SeminarCustomerCome
    permission_classes = [IsSuperuserOrOwner]


class SeminarCustomerBackup(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = SeprateCustomer
    permission_classes = [permissions.IsAdminUser]
