# Home RF Control

This is a small home project to control some of my RF devices using a YARD Stick One and a RESTful API. THe devices include things like fireplace remotes and ceiling fans.  The RESTful server is Python-based and I have it running on a RaspberryPi, where the YARD Stick One is also connected.

This can be integrated with something like Smartthings or Home Assistant to control these devices through a mobile app. I will post instructions on how to create Smartthings device handlers to make requests to the web server.

## Capturing and Decoding the RF signals
This is the most complicated part. I used a combination of the HackRF One with the hackrf_transfer and inspectrum tool to determine the parameters of the signal being transmitted.  These parameters include things like the transmit frequency, bit rate, and the bit stream/pattern for each of the buttons pressed.  Using the FCC ID on the remote and the FCC website helped identify the transmit frequency so I knew where to start looking for the signal.

## Devices
Here are some details of device that I have automated in my house so far:
* Fireplace remote (model: )
* Hunter Light/Ceiling Fan (model: )
* minkaAire (model: TR110A)
  - FCCID: KUJCE10007
