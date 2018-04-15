from django.shortcuts import render
from scoutingdata import models
 
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
    # get list of events for this team
    
    return render(request, 'scoutingdata/team.html', {'teamNum':teamNum})

def event(request, eventCode):
    return render(request, 'scoutingdata/event.html', {'eventCode':eventCode})