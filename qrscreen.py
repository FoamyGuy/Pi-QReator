import web
import PyQRNative
import pygame
import os
urls = (
  '/q', 'QR',
  '/', 'Index',
  '/Dream', 'Dream'
)

os.environ['SDL_VIDEODRIVER'] = 'fbcon'
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"
pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen.fill((255,255,255))
pygame.mouse.set_visible(False)
pygame.display.update()




def makeQR(data_string,path,level=2, boxSize=4):
    quality={1: PyQRNative.QRErrorCorrectLevel.L,
             2: PyQRNative.QRErrorCorrectLevel.M,
             3: PyQRNative.QRErrorCorrectLevel.Q,
             4: PyQRNative.QRErrorCorrectLevel.H}
    size=1
    while 1:
        try:
            print "trying size %s" % size
            q = PyQRNative.QRCode(size,quality[level], boxSize=boxSize)
            q.addData(data_string)
            q.make()
            im=q.makeImage()
            im.save(path,format="png")
            break
        except TypeError:
            print "failed increasing size"
            size+=1
class Index:
    def GET(self):
        _index = '''<html>
        <head>
        <title>ROI-QR</title>
        </head>
        <body>
        <h1>Welcome to ROIQR.com!</h1>
        </body>
        </html>'''
        return _index
class Dream:
    def GET(self):
	screen.fill((20,100,200))
	pygame.display.update()
        return "DREAM BIG"
class QR:
    def GET(self):
        args = web.input(name = 'web')
	print 'making qr'
        try:
            pixelSize = args.size
        except:
            pixelSize = 5

        try:
            lvl = args.lvl
        except:
            lvl = 2
        try:
            data = args.data
            print data
            #web.header('Content-Type','image/png; charset=utf-8', unique=True)
            makeQR(args.data, 'QRfile.png', level=int(lvl), boxSize=int(pixelSize))
            #makeQR("<3 You", 'QRfile.png', boxSize=int(pixelSize))
            f = open('QRfile.png', 'rb')
            imgData = f.read()
            f.close()
	    
            qr_img = pygame.image.load("QRfile.png")
            
            x = (screen.get_width()/2) - (qr_img.get_rect().size[0]/2)
            y = (screen.get_height()/2) - (qr_img.get_rect().size[1]/2)
            screen.blit(qr_img,(x,y))
            pygame.display.update()
            return "OK"
        except Exception as e:
            _error = "You must pass parameter 'data'"
            return str(e)


if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
