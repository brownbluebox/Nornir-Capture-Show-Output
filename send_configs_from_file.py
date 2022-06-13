from unittest import runner
from click import command
from nornir import InitNornir
from nornir_scrapli.tasks import send_configs_from_file
from nornir_utils.plugins.functions import print_result

#define config file folder
config_path="config_list/"

#creating Nornir Object
nr = InitNornir(config_file="config.yaml")

#function to send config using file $config_path/<hostname>.txt
def configure_device(task):
    task.run(task=send_configs_from_file, file=config_path+task.host['config_file'])

results = nr.run(task=configure_device)
print_result(results)
