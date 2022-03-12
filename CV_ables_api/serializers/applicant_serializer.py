from rest_framework import serializers
from CV_ables_api.models import Applicant
from CV_ables_api.serializers.user_serializer import UserSerializer

class ApplicantSerializer(serializers.ModelSerializer):
    user = UserSerializer(many = False)
    class Meta:
        model = Applicant
        fields = ('id', 'github_url', 'user' )