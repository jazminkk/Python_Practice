import base64

def pic2py(picture_name):
    open_pic = open("%s" % picture_name, 'rb')
    b64str = base64.b64encode(open_pic.read())
    open_pic.close()
    write_data = 'img = "%s"' % b64str.decode()
    f = open('%s.py' % picture_name.replace('.', '_'), 'w+')
    f.write(write_data)
    f.close()


pic2py("/Users/sandy/PycharmProjects/Pomodoro/tomato.png")
print("ok")