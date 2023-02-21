from rest_framework import serializers
from MessageApp.models import Messages,Profiles
class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model=Messages
        fields=('MessageId','fromUser','toUser')

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model=Profiles
        fields=('profileId','emailId','firstName','lastName','profilePhotoUrl')