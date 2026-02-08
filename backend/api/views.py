"""
API Views for the Facts API
This module contains all API endpoints for serving facts data
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def get_facts(request):
    """
    API Endpoint: GET /api/facts/
    
    Returns a hardcoded list of interesting facts in JSON format.
    No database required - data is stored in memory.
    
    Response Format:
    {
        "success": true,
        "count": <number_of_facts>,
        "data": [
            {
                "id": 1,
                "fact": "...",
                "category": "..."
            },
            ...
        ]
    }
    """
    
    # Hardcoded list of interesting facts
    facts_data = [
        {
            "id": 1,
            "fact": "Python was named after the comedy series 'Monty Python's Flying Circus', not the snake!",
            "category": "Programming"
        },
        {
            "id": 2,
            "fact": "The first computer bug was an actual bug - a moth found in a Harvard computer in 1947.",
            "category": "Technology"
        },
        {
            "id": 3,
            "fact": "Django framework was named after jazz guitarist Django Reinhardt.",
            "category": "Programming"
        },
        {
            "id": 4,
            "fact": "The '@' symbol in email addresses was chosen in 1971 and is called 'at sign'.",
            "category": "Technology"
        },
        {
            "id": 5,
            "fact": "React was created by Facebook and released as open source in 2013.",
            "category": "Programming"
        },
        {
            "id": 6,
            "fact": "The first website ever created is still online at info.cern.ch.",
            "category": "Internet"
        },
        {
            "id": 7,
            "fact": "GitHub was launched in 2008 and now hosts over 200 million repositories.",
            "category": "Development"
        },
        {
            "id": 8,
            "fact": "The term 'debugging' was popularized by Grace Hopper, a computer science pioneer.",
            "category": "Technology"
        },
        {
            "id": 9,
            "fact": "JavaScript was created in just 10 days by Brendan Eich in 1995.",
            "category": "Programming"
        },
        {
            "id": 10,
            "fact": "The first domain name ever registered was Symbolics.com on March 15, 1985.",
            "category": "Internet"
        }
    ]
    
    # Build response
    response_data = {
        "success": True,
        "count": len(facts_data),
        "message": "Facts retrieved successfully",
        "data": facts_data
    }
    
    return Response(response_data, status=status.HTTP_200_OK)
