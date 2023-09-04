from django.shortcuts import render, redirect
from .models import Voter, Candidate
from .form import VoterForm
from django.http import HttpResponseRedirect

def home(request):
    return render(request, "home.html", {})

def login(request):
    if request.method == 'POST':
        voter_id = request.POST['voter_id']
        password = request.POST['password']
        try:
            voter = Voter.objects.get(voter_id=voter_id, password=password)
            # Successful login            
            # You can perform additional actions here, such as setting session variables
            request.session['voter_id'] = voter.voter_id
            return redirect('voting_page')  # Change this to the URL name of your dashboard
        except Voter.DoesNotExist:
            return render(request, 'login.html', {'error_message': 'Invalid voter ID or password.'})
    return render(request, 'login.html')

def voting_page(request):
    error_message = '' 
    if request.method == 'POST':
        selected_candidate_id = request.POST.get('Candidate')
        if selected_candidate_id:
            try:
                selected_candidate = Candidate.objects.get(cid=selected_candidate_id)
                
                voter_id = request.session.get('voter_id')  # Retrieve voter_id from the session

                if voter_id:
                    # Check if the voter has already voted
                    if not Voter.objects.filter(voter_id=voter_id).exists():
                        Voter.objects.create(voter_id=voter_id, candidate=selected_candidate)
                        
                        print("voted:",selected_candidate.voted)

                        return redirect('vote_count')  # Redirect to a success page after voting
                    else:
                        voter = Voter.objects.get(voter_id=voter_id)
                        if not voter.is_voted:
                            selected_candidate.voted+=1
                            selected_candidate.save()
                            voter.is_voted = True
                            voter.save()
                        else:
                            error_message = "You are already voted"
                else:
                    return redirect('login')  # Redirect to login page if voter_id is not in session

            except Candidate.DoesNotExist:
                error_message = 'Invalid candidate selection.'

    candidates = Candidate.objects.all()
    return render(request, 'voting_page.html', {'candidates': candidates, 'error_message': error_message})

def register(request):
    submitted = False
    if request.method == "POST":
        form = VoterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register?submitted=True')
    else:
        form = VoterForm
        if 'submitted' in request.GET:
            submitted =True
    form = VoterForm
    return render(request, "register.html", {'form':form, 'submitted':submitted})


def vote_count(request):
    candidate  = Candidate.objects.all()
    for i in candidate:
        print(i.voted)
    return render(request, "votecount.html", {'candidate':candidate})