from rest_framework import serializers
from CV_ables_api.models import Jobtype
class JobtypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Jobtype
        fields = (
            'id',
            'label'
        )