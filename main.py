from jinja2 import Environment, FileSystemLoader
import os
import pdfkit
import typer

def generate_cover_letter(company, position):
    env = Environment(loader = FileSystemLoader(os.getcwd()))
    template = env.get_template('cover_letter_template.html')

    with open('out/cover_letter.html', 'w') as fh:
        fh.write(template.render(
            company = company,
            position = position
        ))
    fh.close()

    options = {
        'margin-top': '1in',
        'margin-right': '1in',
        'margin-bottom': '1in',
        'margin-left': '1in',
        'encoding': "UTF-8",
    }

    pdfkit.from_file('out/cover_letter.html', f'out/cover_letter_{company}.pdf', options=options)

def main(company: str, position: str):
    generate_cover_letter(company, position)

if __name__ == "__main__":
    typer.run(main)