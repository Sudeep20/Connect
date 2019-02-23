from rest_framework import serializers

from .models import Form


class FormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Form
        fields = ('id', 'fullname', 'email', 'mobile', 'city', 'gender', 'department', 'hiredDate', 'isPermanent')
