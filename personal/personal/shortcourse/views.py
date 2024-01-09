from django.shortcuts import render,redirect
from shortcourse.models import *
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.
def main(request):
    ob = Courses.objects.all()
    return render(request, 'index.html',{'val' : ob })

def data(request):
    print(request.GET)
    ob = Courses.objects.all()
    data=[]
    for i in ob:
        row={"name":i.name,"description":i.description,"duration":i.duration,"status":i.status,"amount":i.amount,"lid":i.id}
        data.append(row)
    print(data)
    return JsonResponse(data, safe=False)

def add_page(request):
    return render(request, 'adding.html')

def course_add(request):
    name = request.POST['course']
    description = request.POST['description']
    amount = request.POST['amount']
    duration = request.POST['duration']
    status = request.POST['status']

    ob = Courses()
    ob.name = name
    ob.description = description
    ob.amount = amount
    ob.duration = duration
    ob.status = status
    ob.save()

    return HttpResponse('''<script>alert("success");window.location="/"</script>''')

def update(request,id):
    ob = Courses.objects.get(id=id)
    request.session['sid'] = id
    return render(request, 'update_page.html',{'val':ob})

def new_data(request):

    name = request.POST['course']
    description = request.POST['description']
    amount = request.POST['amount']
    duration = request.POST['duration']
    status = request.POST['status']

    ob = Courses.objects.get(id=request.session['sid'])
    ob.name = name
    ob.description = description
    ob.amount = amount
    ob.duration = duration
    ob.status = status
    ob.save()

    return HttpResponse('''<script>alert("success");window.location="/"</script>''')

def delete_course(request, id):

    ob = Courses.objects.get(id=id)
    ob.delete()

    return HttpResponse('''<script>alert("success");window.location="/"</script>''')

def account(request):
    ob = Login.objects.get(id=1)
    return render(request,'profile.html',{'val':ob})

def save_pass(request):

    password = request.POST['password']

    ob = Login.objects.get(id=1)
    ob.password = password
    ob.save()

    return HttpResponse('''<script>alert("success");window.location="/account"</script>''')