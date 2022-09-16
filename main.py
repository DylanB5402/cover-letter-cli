from jinja2 import Environment, FileSystemLoader
import os
import pdfkit

env = Environment(loader = FileSystemLoader(os.getcwd()))
template = env.get_template('cover_letter_template.html')

with open('cover_letter.html', 'w') as fh:
    fh.write(template.render(
        company = 'Appfolio',
        position = 'Software Engineer Intern'
    ))
fh.close()

options = {
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
}

pdfkit.from_file('cover_letter.html', 'cover_letter.pdf', options=options)
