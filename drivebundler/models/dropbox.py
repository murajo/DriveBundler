# coding=utf-8
import os
from drivebundler.consts import PREF_CHOICE
from django.db import models
import dropbox
# Create your models here.
class Dropbox(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def print_test():
        return 'aaa'

    # ファイルアップロード
    def drive_upload(source_file, destination_path):
        dbx = dropbox.Dropbox(PREF_CHOICE['DROPBOX_ACCESS_TOKEN'])
        dbx.users_get_current_account()
        f = open(source_file, 'rb')
        dbx.files_upload(f.read(),destination_path)
        f.close()
        return

    # アプリディレクトリにあるフォルダ,ファイルの一覧を返す
    def drive_read():
        dbx = dropbox.Dropbox(PREF_CHOICE['DROPBOX_ACCESS_TOKEN'])
        file_list = []
        folder_list = []
        for entry in dbx.files_list_folder('').entries:
            if entry.name.count('.'):
                file_list.append(entry.name)
            else:
                folder_list.append(entry.name)
        return folder_list

    # ファイルダウンロード
    def drive_download():
        dbx = dropbox.Dropbox(PREF_CHOICE['DROPBOX_ACCESS_TOKEN'])
        #dbx.files_create_folder('/' + "server")
        metadata,f = dbx.files_download('/client.json')
        out = open(os.environ['HOME'] + "/checks", 'wb')
        out.write(f.content)
        out.close()
        return f

    # ディレクトリ作成
    def create_folder(path, name):
        dbx = dropbox.Dropbox(PREF_CHOICE['DROPBOX_ACCESS_TOKEN'])
        dbx.files_create_folder(path + name)
