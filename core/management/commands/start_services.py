from django.core.management.base import BaseCommand
import subprocess
import os
import sys
import time

class Command(BaseCommand):
    help = 'Start Django server along with Celery, run migrations, collect static files, and more.'

    def handle(self, *args, **kwargs):
        # Define the commands to be executed
        commands = [
            # Make migrations
            'python manage.py makemigrations',
            # Apply migrations to the database
            'python manage.py migrate',
            # Celery migrate result backend
            ' python manage.py migrate django_celery_results'
            # Create or update the superuser (optional)
            # 'python manage.py createsuperuser --noinput || true',
            # Start Celery worker
            #'celery -A molepay worker --loglevel=info',
        ]

        # Execute each command except the server command
        for command in commands:
            self.stdout.write(f'Running command: {command}')
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            
            if process.returncode != 0:
                self.stderr.write(f'Error running command: {command}')
                self.stderr.write(stderr.decode('utf-8'))
                sys.exit(process.returncode)
            else:
                self.stdout.write(stdout.decode('utf-8'))

        # Start Django server in a separate process
        self.stdout.write('Starting Django server...')
        server_process = subprocess.Popen(['python', 'manage.py', 'runserver'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        try:
            while True:
                time.sleep(60)  # Keep the script running
                if server_process.poll() is not None:
                    break
        except KeyboardInterrupt:
            self.stdout.write('Stopping server...')
            server_process.terminate()
