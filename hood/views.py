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