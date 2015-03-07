from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from polls.models import Poll

# Create your views here.
def index(request):
    return render(request, 'polls/index.html')

def top_commenters(request):
    """just returns contents of top_commenters.json"""

    with open('polls/top_commenters.json', 'r') as f:
        data = f.read()
    return HttpResponse(data, content_type="application/json")


def poll_results_json(request, poll_thread_id):
    poll = get_object_or_404(Poll, thread_id=poll_thread_id)
    if poll.is_active:
        data = poll.json_results
    else:
        data = json.dumps(poll.status.name)

    return HttpResponse(data, content_type="application/json")

def poll_detail(request, slug):
    poll = get_object_or_404(Poll, slug=slug)
    data = {'poll': poll}
    return render(request, 'polls/poll_detail.html', data)

