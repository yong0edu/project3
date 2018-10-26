from django.http import HttpResponse
from django.shortcuts import render

import os

from project3 import settings


def upload1(request):
    if request.method == 'GET':
        return render(
            request,
            'file/upload1.html',
            {})
    else:
        upload_file = request.FILES['my_file']
        login_id = request.session['id']
        try:
            os.mkdir(login_id) #디렉토리 생성
        except FileExistsError:
            pass
        with open(login_id+ '/' + upload_file.name, 'wb') as file:
            for chunk in upload_file.chunks():
                file.write(chunk)
        return HttpResponse('완료' + upload_file.name)



def upload2(request):
    if request.method == 'GET':
        return render(
            request,
            'file/upload2.html',
            {})
    else:
        upload_files = request.FILES.getlist('my_file')
        for upload_file in upload_files:
            with open('file/' + upload_file.name, 'wb') as file:
                for chunk in upload_file.chunks():
                    file.write(chunk)

        return HttpResponse('완료'+ upload_file.name)




def login(request, id):
    request.session['id'] = id
    return HttpResponse('Login!')



def download(request):
    filepath = os.path.join(settings.BASE_DIR, 'yong/function1.html')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
