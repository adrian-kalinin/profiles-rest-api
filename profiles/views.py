from rest_framework.response import Response
from rest_framework.views import APIView


class HelloApiView(APIView):
    """Simple APIView example"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        apiview_features = [
            "Uses HTTP methods as functions (get, post, patch, put, delete)",
            "Is similar to a traditional Django View",
            "Gives you the most control over your application logic",
            "Is mapped manually to URLs",
        ]

        return Response({"message": "Hello!", "apiview_features": apiview_features})
