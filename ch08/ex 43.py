import os


def create_dirs(title, auth):
    os.makedirs(f'{title}')
    js = input("Do you want a folder for JavaScript? ")
    if js == 'y':
        os.makedirs(os.path.join(os.path.join(os.getcwd(), title), 'js'))
    css = input("Do you want a folder for CSS? ")
    if css == 'y':
        os.makedirs(os.path.join(os.path.join(os.getcwd(), title), 'css'))
    create_index(title, auth)


def create_index(title, auth):
    with open(os.path.join(os.path.join(os.getcwd(), title), 'index.html'), 'w') as file:
        file.write(f"""<!DOCTYPE html>
        <html>
            <head>
                <title>{title}</title>
                <meta name="author" content="{auth}">
            </head>
            <body>
                <h1>This is the website template.</h1>
            </body>
        </html>""")


site = input("Site name: ")
author = input("Author: ")
create_dirs(site, author)
