import os
import yaml
import argparse

def write_controls_content(control, cf):          
    h1 = '##'
    h2 = '###'
    final_newline = '\n'
    
    cf.write(f'{h1} {control["id"]}\n\n')
    cf.write(f'{h2} Control\n\n')
    cf.write(f'{control["statement"]}\n\n')
    cf.write(f'{h2} Description\n\n')
    cf.write(f'{control["description"]}\n{final_newline}')


def yaml_to_md(input_dir, input_file, for_website):

    with open(input_file, 'r') as f:
        data = yaml.safe_load(f)

    for group in data['groups']:
        group_id = group['id']
        controls = group['controls']

        for file in sorted(os.listdir(input_dir)):
            if "-MASVS-" in file:
                # group_id_in_file is the part of the filename after the first dash and without the extension
                group_id_in_file = file.split("-")[1] + "-" + file.split("-")[2].split(".")[0]
               
                if group_id_in_file == group_id:
                    with open(os.path.join(input_dir, file), "a") as f:
                        if for_website == False:
                            f.write('\n\n## Controls\n')
                        else:
                            f.write('\n<style> table { width: 100%; } </style>\n\n')
                        f.write('| ID | Control |\n')
                        f.write('|----|-----------|\n')
                        for control in controls:
                            if for_website == True:
                                control_id = f'[{control["id"]}](/MASVS/Controls/{control["id"]})'
                            else:
                                control_id = control["id"]
                            
                            f.write(f'| {control_id} | {control["statement"]} |\n')
                        
                        f.write('\n')
                        f.write('<!-- \pagebreak -->\n\n')
                    
                        if for_website == False:
                            for control in controls:
                                write_controls_content(control, f)
                print(f'Successfully wrote to {file}')

# get input arguments
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--input-dir", help="Input Directory", required=False, default="Document")
parser.add_argument("-i", "--input", help="Input file", required=False, default="OWASP_MASVS.yaml")
parser.add_argument("-w", "--website", help="Generate for website", action='store_true', required=False, default=False)
args = parser.parse_args()

input_dir = args.input_dir
input_file = args.input
for_website = args.website

yaml_to_md(input_dir, input_file, for_website)
