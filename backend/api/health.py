"""
Health Check API Endpoint
Provides system status for monitoring and deployment verification
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from django.db.utils import OperationalError


@api_view(['GET'])
def health_check(request):
    """
    API Endpoint: GET /api/health/
    
    Returns the health status of the application.
    Checks database connectivity and overall system status.
    
    Response Format:
    {
        "status": "healthy" | "unhealthy",
        "database": "connected" | "disconnected",
        "debug": true | false
    }
    """
    health_status = {
        "status": "healthy",
        "database": "disconnected",
        "debug": False
    }
    
    # Check database connection
    try:
        connection.ensure_connection()
        health_status["database"] = "connected"
    except OperationalError:
        health_status["database"] = "disconnected"
        health_status["status"] = "unhealthy"
    
    # Include debug status (useful for verification)
    from django.conf import settings
    health_status["debug"] = settings.DEBUG
    
    # Return 200 if healthy, 503 if unhealthy
    response_status = status.HTTP_200_OK if health_status["status"] == "healthy" else status.HTTP_503_SERVICE_UNAVAILABLE
    
    return Response(health_status, status=response_status)
