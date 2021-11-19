from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .authenticators import google_authenticator
from .serializers import InputSerializer


@api_view(["POST"])
def login(request):
    input_serializer = InputSerializer(data=request.data)
    input_serializer.is_valid(raise_exception=True)

    validated_data = input_serializer.validated_data
    provider = validated_data.get("provider")
    if provider == "google":
        response = google_authenticator(validated_data)
        return Response(response)
    else:
        raise ValidationError(
            {"error": f"Provider {provider} not currently supported."}
        )
