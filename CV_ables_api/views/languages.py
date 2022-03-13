from rest_framework.decorators import api_view
from rest_framework.response import Response
from CV_ables_api.models import Language, language
from CV_ables_api.serializers import LanguageSerializer

@api_view(['GET'])
def get_language_list(self):
    language = Language.objects.all()
    
    serializer = LanguageSerializer(language, many=True)
    return Response(serializer.data)