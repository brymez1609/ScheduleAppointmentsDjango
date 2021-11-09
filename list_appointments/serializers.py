from rest_framework import serializers

from list_appointments.models import CustomSettings

class HelloSerializer(serializers.Serializer):
    hello = serializers.CharField()
    cantidad = serializers.IntegerField()   
    url = serializers.CharField() 

class CustomSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomSettings
        fields = '__all__'

    def create(self, validated_data):
        custom_setting_object = CustomSettings(**validated_data)
        custom_setting_object.save()
        print("saved")
        return custom_setting_object    