import os, shutil

from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Sets e-mail host, secret_key'

    def add_arguments(self, parser):
        parser.add_argument('user', type=str, help='Sets e-mail user')
        parser.add_argument('password', type=str, help='Sets e-mail password')
        parser.add_argument('secret_key', type=str, help='Sets Django secret_key')

    def handle(self, *args, **options):
        user = options['user']
        password = options['password']
        secret_key = options['secret_key']

        path = 'secret_files/'

        #check existence of secret_files directory
        if os.path.exists(path):
            shutil.rmtree(path)

        #creating secret_files directory
        os.mkdir(path)
        os.chdir(path)

        #email host settings
        email_host = open('email_host.txt', 'w', encoding='utf-8')
        email_host.write(user+'\n')
        email_host.write(password)
        email_host.close()

        #secret_key settings
        secret_key_file = open('secret_key.txt', 'w', encoding='utf-8')
        secret_key_file.write(secret_key)
        secret_key_file.close()

        print('Settings were successfully set')
