import os

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from drivebundler.models.google import Google
from drivebundler.models.dropbox import Dropbox


# Create your views here.

def index(request):
    home_path = os.environ['HOME']
    file_dir_list = os.listdir(home_path)
    list_clear = []
    #隠しファイル取り除く
    for x in file_dir_list:
        if("." != x[:1]):
            list_clear.append(x)
    list_file = [f for f in list_clear if os.path.isfile(os.path.join(home_path, f))]
    list_dir = [f for f in list_clear if os.path.isdir(os.path.join(home_path, f))]
    params = {
        'list_dir': list_dir,
        'list_file': list_file
    }
    return render(request, 'drivebundler/index.html', params)

def google(request):
    test = 'google'
    test = Google.print_test()
    params = {
        'test' : Google.print_test(),
        'title' : "a"
    }
    if request.method == "POST":
        params['title'] = request.POST.get("title")
        text = request.POST.get("text")
        Google.drive_write(params['title'], text)
    return render(request, 'drivebundler/google.html', params)

def dropbox(request):
    result = ''
    if request.method == "POST":
        if request.POST.get("submit") == "upload":
            source_path = request.POST.get("upload_source")
            destination_path = "/" + request.POST.get("upload_destination")
            Dropbox.drive_upload(source_path, destination_path)
        elif request.POST.get("submit") == "download":
            source_path = request.POST.get("download_source")
            destination_path = request.POST.get("download_destination")
            Dropbox.drive_download(source_path,destination_path)
        result = request.POST.get("submit")
    file_list, folder_list = Dropbox.drive_read()
    params = {
        'file_list': file_list,
        'folder_list': folder_list,
        'result':result
    }
    return render(request, 'drivebundler/dropbox.html', params)
