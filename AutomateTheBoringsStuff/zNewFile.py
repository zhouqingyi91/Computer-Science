def createFile(title, url):
    from os import path
    # title = title.replace('.', '')
    # split = title.split()
    newtitle = ''

    for word in title.replace('.', '').split():
        newtitle += word + '-'

    name = newtitle[:len(newtitle) - 1] + '.py'

    destination = './'

    if not (path.isfile(destination + name)):
        f = open(destination + name, 'w')
        f.write('# Question url:\n# {}\n'.format(url))
        f.close()
        print('Done')
    else:
        print('file already exist')


title = ''
url = ''
createFile(title, url)
