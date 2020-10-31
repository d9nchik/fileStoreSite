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
            # m = sha3_256()
            file_ = request.FILES['file']
            id = get_id(5)
            instance = File(path=file_, name=request.POST['name'], unique=id)
            # instance.path.open()
            # m.update(instance.path.read())
            # instance.id = m.hexdigest()
            instance.save()
            return HttpResponseRedirect('/success/url/{}'.format(id))
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def get_id(number_of_symbols: int) -> str:
    return hex(int(time() % (16 ** number_of_symbols)))[2:]


def get_file(request, file_unique):
    print(file_unique)
    try:
        file = File.objects.get(unique=file_unique).path  # get the string you want to return.
        return FileResponse(file)
    except File.DoesNotExist:
        return HttpResponse(f'<h1>What are you looking here)</h1>')


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
