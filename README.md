Pi-QReator
==========

Web app that is meant to be run on Raspberry Pi with [2.8" TFT Touchscreen](https://www.adafruit.com/products/1601)

You can send it a request with some data, it will encode the data into a QR code and then show it on the screen.

Requirements
------------
* [webpy](http://webpy.org/)
* [PIL](http://pillow.readthedocs.org/en/latest/)
* [PyQRNative](https://code.google.com/p/pyqrnative/)

To get requirements
-------------------
    $ sudo pip install web.py
    $ sudo pip install Pillow


To launch the app
-----------------
    $ sudo python qrscreen.py
    
To use
------
Send GET request: http://[your-pi]:8080/q?data=HelloWorld