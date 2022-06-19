from django.shortcuts import render

# Create your views here.
def index (request): 
    '''
    View function that returns the landing page and its data
    '''   
    return render(request, 'index.html')

# @login_required(login_url='login')
def join_hood(request):
    '''
    View function that renders the neighborhood page and its data
    '''
    # neighbourhood =get_object_or_404(neighbourhood,id=id)
    # request.user.profile.neighbourhood =neighbourhood
    # request.user.profile.save()
    # return redirect('hood')
    return render(request, 'single_hood.html')

# @login_required(login_url='login')
def profile(request):
    '''
    View function that renders the profile page and its data
    '''
    return render(request, 'profile.html')

def login_user(request):
    '''
    View function that renders the login page and its data
    '''
    return render(request, 'auth/login.html')

def signup(request):
    '''
    View function that renders the signup page and its data
    '''
    # if request.method == 'POST':
    #     form = SignupForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password1')
    #         user = authenticate(username=username, password=password)
    #         login(request, user)
    #         return redirect('index')
    # else:
    #     form = SignupForm()
    return render(request, 'auth/signup.html', locals())