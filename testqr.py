import PyQRNative


def makeQR(data_string,path,level=2, boxSize=4):
    quality={1: PyQRNative.QRErrorCorrectLevel.L,
             2: PyQRNative.QRErrorCorrectLevel.M,
             3: PyQRNative.QRErrorCorrectLevel.Q,
             4: PyQRNative.QRErrorCorrectLevel.H}
    size=1
    q = PyQRNative.QRCode(size,quality[level], boxSize=boxSize)
    q.addData(data_string)
    q.make()
    im=q.makeImage()
    im.save(path,format="png")

makeQR("hello","qr.png",2,5 )
#qr = QRCode(1, QRErrorCorrectLevel.M)
#qr.addData("hello")

#qr.make()

#im = qr.makeImage()

#im.save("qr.png")
