from hashlib import sha3_256
from time import time

from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, FileResponse, HttpResponse
from django.shortcuts import render

from myfiles.form import UploadFileForm
from myfiles.models import File


# Create your views here.
def upload_file(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_ = request.FILES['file']
            id = get_id(5)
            instance = File(path=file_, name=request.POST['name'], unique=id)
            hashName(instance.path)
            instance.save()
            return HttpResponseRedirect('/links'.format(id))
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def hashName(file_field):
    m = sha3_256()
    file_field.open()  # make sure we're at the beginning of the file
    m.update(file_field.read())
    ext = file_field.name.split('.')[-1]
    file_field.name = m.hexdigest() + '.' + ext


def get_id(number_of_symbols: int) -> str:
    return hex(int(time() % (16 ** number_of_symbols)))[2:]


def get_file(request, file_unique):
    try:
        object = File.objects.get(unique=file_unique)
        file = object.path  # get the string you want to return.
        response = FileResponse(file, filename=object.name + '.' + file.name.split('.')[-1])
        return response
    except File.DoesNotExist:
        return HttpResponse(f'<h1>What are you looking here)</h1>')


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'


def get_links(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    try:
        links = File.objects.order_by('-date_of_upload')
        return render(request, 'links.html', {'links': links})
    except File.DoesNotExist:
        return HttpResponse(f'<h1>Oops. Contact master</h1>')
