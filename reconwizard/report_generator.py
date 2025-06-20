from jinja2 import Environment , FileSystemLoader
import os 
def generate_html_report(data,output_path):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report_template.html')
    with open(output_path, 'w') as f:
        f.write(template.render(**data))
