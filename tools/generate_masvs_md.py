import os
import yaml
import argparse

def write_controls_content(control, cf, for_website):
    h1 = '#'
    h2 = '##'
    final_newline = ''

    if for_website == False:            
        h1 = '##'
        h2 = '###'
        final_newline = '\n'
    
    cf.write(f'{h1} {control["id"]}\n\n')
    cf.write(f'{h2} Statement\n\n')
    cf.write(f'{control["statement"]}\n\n')
    cf.write(f'{h2} Description\n\n')
    cf.write(f'{control["description"]}\n{final_newline}')


def yaml_to_md(input_file, for_website):

    dirname = "controls"
    if not os.path.exists(dirname):
        os.mkdir(dirname)

    with open(input_file, 'r') as f:
        data = yaml.safe_load(f)

    file_index = 5 # the first MASVS chapters are 01-04

    for group in data['groups']:
        title = group['title']
        group_id = group['id']
        desc = group['description']
        controls = group['controls']
        
        if for_website == True:
            filename = f'{group_id}.md'
        else:
            filename = f'Document/{file_index:02d}-{group_id}.md'  
          
        with open(filename, 'w') as f:
            f.write(f'# {group_id}: {title}\n\n')
            # f.write('## Description\n\n')
            f.write(f'{desc}\n\n')
            # f.write('## Controls\n\n')
            f.write('| ID | Statement |\n')
            f.write('|----|-----------|\n')
            for control in controls:
                if for_website == True:
                    control_id = f'[{control["id"]}](controls/{control["id"]})'
                else:
                    control_id = control["id"]
                
                f.write(f'| {control_id} | {control["statement"]} |\n')
            
            f.write('\n')
            f.write('<!-- \pagebreak -->\n')

            for control in controls:
                if for_website == True:
                    # Create the filename for the output file
                    control_filename = f'{dirname}/{control["id"]}.md'  
                    with open(control_filename, 'w') as cf:
                        write_controls_content(control, cf, for_website)
                else:
                    write_controls_content(control, f, for_website)
        file_index += 1
        print(f'Successfully wrote {filename}')

# get input arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Input file", required=False, default="masvs.yaml")
parser.add_argument("-w", "--website", help="Generate for website", action='store_true', required=False, default=False)
args = parser.parse_args()

input_file = args.input
for_website = args.website

yaml_to_md(input_file, for_website)
