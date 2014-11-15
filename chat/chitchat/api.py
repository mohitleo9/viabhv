from chitchat.models import Message
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def message_get_handler(request):
    """
    Handles the get request for message
    """
    # let the user see his data
    # only show text and date
    data = Message.objects.filter(user=request.user).values('text', 'date')

    # now we need to convert date to readable format
    for d in data:
        d['date'] = d['date'].strftime('%A, %B %d, %Y at %H:%M hours')

    # http://stackoverflow.com/questions/26067369/how-to-pass-model-fields-to-a-jsonresponse-object
    return JsonResponse(dict(response_json=list(data)))
