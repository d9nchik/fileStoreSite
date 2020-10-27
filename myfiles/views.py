from django.http import HttpResponseRedirect, FileResponse, HttpResponse
from django.shortcuts import render
from myfiles.models import File
from myfiles.form import UploadFileForm
from hashlib import sha3_256
from django.core.files.base import ContentFile


# Create your views here.
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            m = sha3_256()
            file_ = request.FILES['file']
            instance = File(path=file_, name=request.POST['name'])
            instance.path.open()
            m.update(instance.path.read())
            instance.unique = m.hexdigest()
            instance.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def get_file(request):
    if request.method == 'GET' and 'id' in request.GET:
        id = request.GET['id']
        try:
            file = File.objects.get(unique=id).path  # get the string you want to return.
            return FileResponse(file)
        except File.DoesNotExist:
            pass
    return HttpResponse(f'<h1>What are you looking here)</h1>')
