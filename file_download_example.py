import requests
url = 'https://readthedocs.org/projects/django/downloads/pdf/latest/'
r = requests.get(url, allow_redirects=True)  # to get content after redirection
pdf_url = r.url # 'https://media.readthedocs.org/pdf/django/latest/django.pdf'
with open('file_name.pdf', 'wb') as f:
    f.write(r.content)

# r = requests.head(url, allow_redirects=True)  # to get only final redirect url