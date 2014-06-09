import web
import PyQRNative
import pygame
import os

# List of URLs for webpy server
urls = (
  '/q', 'QR',
  '/', 'Index',
  '/Dream', 'Dream',
  '/clear', 'Clear'
)

# Variables needed to enable the TFT screen
os.environ['SDL_VIDEODRIVER'] = 'fbcon'
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen.fill((255,255,255))
pygame.mouse.set_visible(False)
pygame.display.update()



"""
Helper method that will try to create the smallest version QR possible
given the input data string. 
For more info on versions see here: http://www.qrcode.com/en/about/version.html
"""
def makeQR(data_string,path,level=2, boxSize=4, color=(0,0,0,255)):
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
            img = im.convert("RGBA")
            #Color
            if color != (0,0,0,255):
                print "Given color is not black"
                
                pixdata = img.load()

             
                # If pixel is black change to desired color. 
                for y in xrange(img.size[1]):
                    for x in xrange(img.size[0]):
                        if pixdata[x, y] == (0, 0, 0, 255):
                            pixdata[x, y] = color

            img.save(path,format="png")
            break
        except TypeError as te:
            print "failed increasing size"
            print str(te)
            size+=1

"""
url: /
detail: serve the form which will allow you to choose data
        and parameters for creating a QR.
"""
class Index:
    def GET(self):
       raise web.seeother("/static/landing.html") 
"""
url: /Dream
detail: Currently unused.
        Except to clear the screen, and deliver a positive message =)
"""
class Dream:
    def GET(self):
	screen.fill((20,100,200))
	pygame.display.update()
        return "DREAM BIG"

"""
url: /clear
detail: clear the screen, reset it back to white.
"""
class Clear:
    def GET(self):
	screen.fill((255,255,255))
	pygame.display.update()
	return "OK"


"""
url: /q
detail: endpoint used to create QR code and show it on the screen.
args: data - (required) string which will get encoded in the QR
      size - size in px of each 'box' within the QR. 4 works pretty well.
      lvl - Error correction level, acceptable values 1-4
      color - comma separated RGBA value ex. 0,0,255,255
"""
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
            color = tuple(map(int,str(args.color).split(',')))
        except:
            color = (0,0,0,255)

        try:
            data = args.data
            print(color)
            makeQR(args.data, 'QRfile.png', level=int(lvl), boxSize=int(pixelSize), color=color)
            qr_img = pygame.image.load("QRfile.png") 
            x = (screen.get_width()/2) - (qr_img.get_rect().size[0]/2)
            y = (screen.get_height()/2) - (qr_img.get_rect().size[1]/2)
            screen.fill((255,255,255))
            screen.blit(qr_img,(x,y))
            pygame.display.update()
            return 'OK'
        except Exception as e:
            if str(e) == "'data'":
	        return "You must pass parameter 'data'"
            return str(e)


if __name__ == "__main__":
        # Start the server
	app = web.application(urls, globals())
	app.run()
