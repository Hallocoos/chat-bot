from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import logging
import json
from django.http import JsonResponse
from .models import Conversation
import json


logger = logging.getLogger(__name__)

@csrf_exempt
def get_status(request):
    """
    Endpoint to return a status response.
    """
    return JsonResponse({"status": "ok"})

@api_view(['POST'])
def get_chat_response(request):
    """
    Endpoint to handle chat interactions.
    Requires authentication with token.
    """
    data = json.loads(request.body)
    # if id doesn't exist:
    #   createNewConversation();
    # else:
    #   findNextQuestion();
    userid = data.get('userid')
    conversationid = data.get('conversationid')
    optionpicked = data.get('optionpicked')
    state = data.get('state')

    try:
        data = json.loads(request.body)
        userid = data.get('userid')
        conversationid = data.get('conversationid')
        optionpicked = data.get('optionpicked')
        state = data.get('state')

        conversation = Conversation.objects.create(userid=userid, conversationid=conversationid, optionpicked=optionpicked, state=state)
        return JsonResponse({'status': 'success', 'message': 'Conversation data saved successfully'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
