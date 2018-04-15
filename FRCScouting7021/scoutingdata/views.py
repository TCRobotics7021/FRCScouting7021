from django.shortcuts import render
from scoutingdata import models
import requests, json, logging

api_key = ""
endpoint = "https://www.thebluealliance.com/api/v3/"
 
# Create your views here.
def home(request):
    return render(request, 'scoutingdata/home.html')

def loginview(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return redirect('home')
        else:
            # Invalid
            return render(request, 'accounts/login.html', {"error":"The username and password didn't match."})
    else:
        return render(request, 'accounts/login.html')

def team(request, teamNum):
    logger = logging.getLogger(__name__)
    logger.error('Team Num: ' + str(teamNum))
    # get list of events for this team
    # https://www.thebluealliance.com/api/v3/team/{TEAM_CODE}/events/simple
    
    call = endpoint + "team/frc" + str(teamNum) + "/events/simple"

    r = requests.get(call, headers={'X-TBA-Auth-Key':api_key})

    if r.status_code == 200:
        # successful call
        logger.error('it worked')
    else:
        # unsuccessful call
        return render(request, 'scoutingdata/event.html', {"error":"Could not retrieve team events."})

    return render(request, 'scoutingdata/team.html', {'teamNum':teamNum})

def event(request, eventCode):
    return render(request, 'scoutingdata/event.html', {'eventCode':eventCode})