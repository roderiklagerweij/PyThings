__author__ = 'Roderik'


def write_template(images):
    f = open('template/template.html', 'r')
    template = f.read()
    f.close()

    f = open('images/index.html', 'w')

    imgs = ''
    for image in images:
        imgs += '<img src="' + image + '.png" style="padding: 10px;">'

    template = template.replace('!images!', imgs)
    f.write(template)
    f.close()