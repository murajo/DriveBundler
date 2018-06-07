# coding=utf-8
import os
from drivebundler.consts import PREF_CHOICE
from django.db import models
import dropbox
import logging
import traceback
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

    # アップロード
    def drive_upload(source_file, destination_path, path_log = ''):
        if path_log == '': path = source_file
        else : path = path_log + '/' + source_file
        logging.debug(path_log)
        dbx = dropbox.Dropbox(PREF_CHOICE['DROPBOX_ACCESS_TOKEN'])
        dbx.users_get_current_account()
        source_path = os.path.expanduser('~') + "/" + path
        if os.path.isfile(source_path):
            f = open(source_path, 'rb')
            dbx.files_upload(f.read(),'' + '/' + path)
            f.close()
        elif os.path.isdir(source_path):
            dbx.files_create_folder('/' + source_file)
            Dropbox.folder_conversion(source_path, destination_path + '/' + source_file, path)
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
        return file_list, folder_list

    # ファイルダウンロード
    def drive_download(source_path, destination_path):
        dbx = dropbox.Dropbox(PREF_CHOICE['DROPBOX_ACCESS_TOKEN'])
        try:
            metadata,f = dbx.files_download(source_path)
        except Exception as err_msg:
            # logging.debug("except now")
            # logging.debug(err_msg)
            # logging.debug(type(err_msg))
            debug_msg = traceback.format_exc()
            if debug_msg.count(PREF_CHOICE['DROPBOX_FOLDER_ERROR']):
                logging.debug('joujou')
        else:
            out = open(destination_path, 'wb')
            out.write(f.content)
            out.close()
            return f
        # metadata,f = dbx.files_download(source_path)
        # return f

    #アップロード元がフォルダのときに呼ばれファイルアップロードを繰り返し呼ぶ
    def folder_conversion(source_path, destination_path, path_log):
        list = os.listdir(source_path)
        logging.debug(list)
        for file in list:
            Dropbox.drive_upload(file, destination_path, path_log)
        return

    # ディレクトリ作成
    def create_folder(path, name):
        dbx = dropbox.Dropbox(PREF_CHOICE['DROPBOX_ACCESS_TOKEN'])
        dbx.files_create_folder(path + name)
