from .models import Form
from rest_framework import viewsets
from formapp.serializers import FormSerializer


class FormViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Form.objects.all()
    serializer_class = FormSerializer

