Pi-QReator
==========

Web app that is meant to be run on Raspberry Pi with [2.8" TFT Touchscreen](https://www.adafruit.com/products/1601)

You can send it a request with some data, it will encode the data into a QR code and then show it on the screen.

**Requirements:**  
* [webpy](http://webpy.org/)
* [PIL](http://pillow.readthedocs.org/en/latest/) - I chose Pillow fork
* [PyQRNative](https://code.google.com/p/pyqrnative/) - slightly modified version included

**To get requirements:**  

    $ sudo pip install web.py
    $ sudo pip install Pillow


**To launch the app:**  

    $ sudo python qrscreen.py
    
**To use:**  
Open browser to `http://[your-pi]:8080/`

![picture](http://static.projects.hackaday.com/images/8489501402175975782.jpg)
