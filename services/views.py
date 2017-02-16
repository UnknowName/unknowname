from django.shortcuts import render

def upload_file(request):
    pass
    if request.method == 'POST':
        print request.FILES
        return render(request,'up_file.html',locals())
    else:
        return render(request,'up_file.html',locals())

