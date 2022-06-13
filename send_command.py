from click import command
from nornir import InitNornir
from nornir_scrapli.tasks import send_commands
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

#define output file location
output_file_location="output/"

nr = InitNornir(config_file="config.yaml")

#list command to capture
command_list = [
"show ip interface brief",
"show clock"
]

def write_output(host,output):
    f=open(f"{host}.txt","w")
    f.write(output)
    f.close()

def show_command(task):
    for cmd in command_list:
        task.run(task=send_command, command=cmd, strip_prompt="false")

results=nr.run(task=show_command)

for host in nr.inventory.hosts:
    output=""
    appendix=""
    for cmd in range(len(command_list)):
        appendix=host + "#" + command_list[cmd] + "\n"
        output+=appendix+results[host][cmd+1].result+"\n\n"
    write_output(output_file_location+host,output)
    #print(output)