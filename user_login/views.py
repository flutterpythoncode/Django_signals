from django.shortcuts import render
from user_login.models import *
from django.shortcuts import redirect

# Login page function:-
def dataEnter(request):
    
    try:
        if request.method == "POST":
            get_value= request.POST
            fullname=get_value.get('fullname')
            age=get_value.get('age')
            userData.objects.create(fullname=fullname, age=age)
            return redirect('/')
    except Exception as error:
        raise TypeError(error)
    
    return render(request, 'login_page.html')

def viewRecords(request):
    
    context={'data':userData.objects.all().values()}
    return render(request, 'records.html', context)

def deleteRecord(request, id):
    user=userData.objects.get(id=id)
    user.delete()
    return redirect('/view_records/')
