from django.core.management.base import BaseCommand

from subprocess import Popen, PIPE


class Command(BaseCommand):
    help = 'Run all commands'

    commands = [
        'python manage.py load_fields',
        'python manage.py load_motherboards_data',
        'python manage.py load_cpus_data',
        'python manage.py load_rams_data',
        'python manage.py load_gpus_data',
        'python manage.py load_cases_data',
        'python manage.py load_internal_drives_data',
        'python manage.py load_power_supplies_data',
        'python manage.py load_laptops_data',
        'python manage.py load_mobiles_data',
    ]

    def handle(self, *args, **options):
        proc_list = []

        for command in self.commands:
            print('$ run ' + command)
            proc = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
            stdout, stderr = proc.communicate()
            return_code = proc.returncode

            if return_code != 0:
                print(f"Error: Command '{command}' failed with return code {return_code}")
                print("STDOUT:\n", stdout.decode())
                print("STDERR:\n", stderr.decode())
                break

            print(f"Command '{command}' completed successfully.")

        # try:
        #     while True:
        #         time.sleep(10)
        # except KeyboardInterrupt:
        #     for proc in proc_list:
        #         os.kill(proc.pid, signal.SIGKILL)