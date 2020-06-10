#!/usr/bin/python
import sys
import rflib
import bitstring

class RFDevice(object):
    def _send(self, bin_seq, d):
        #print bin_seq
        rf_data = bitstring.BitArray(bin=bin_seq).tobytes()
        d.setModeTX()
        d.setFreq(self.frequency)
        d.setMdmModulation(self.modulation)
        d.setMdmDRate(self.data_rate)
        d.setMdmSyncMode(0)
        d.makePktFLEN(len(rf_data))
        d.setMaxPower()
        d.RFxmit(rf_data)
        d.setModeIDLE()

    def _expand_tribits(self, bits, ZERO='001', ONE='011'):
        return ''.join(ZERO if b=='0' else ONE for b in bits)

class Fireplace(RFDevice):
    def __init__(self):
        self.frequency = 303870000
        self.modulation = rflib.MOD_ASK_OOK
        self.data_rate = int(1/.00058175)
        self.prefix = '00000001'

    def turnon(self, dongle): 
        on  = '010001101001010001111000'
        bin_seq = (self.prefix + self._expand_tribits(on))*10
        self._send(bin_seq, dongle)

    def turnoff(self, dongle):
        off = '010001101001010001101001'
        bin_seq = (self.prefix + self._expand_tribits(off))*10
        self._send(bin_seq, dongle)


class LivingRoomFan(RFDevice):
    def __init__(self):
        self.frequency = 433900000
        self.modulation = rflib.MOD_ASK_OOK
        self.data_rate = int(1/0.0004)
        self.prefix = '0'*35+'1'
        self.code = None
        
    def set_fan_low(self, dongle):
        low = '111111001000'
        bin_seq = (self.prefix + self._expand_tribits(low)) * 6
        self._send(bin_seq, dongle)
        

class HunterFanLight(RFDevice):
    def __init__(self):
        self.frequency = 433900000
        self.modulation = rflib.MOD_ASK_OOK
        self.data_rate = int(1/0.0004) #0.4ms
        self.prefix = '0'*62 + '01'*12 + '0'*13
        self.code = None

    def toggle_light(self, dongle):
        light_pt1  = self.code + '10001000000001110111111110'
        light_pt2  = self.code + '10000001001101111110110010'
        bin_seq = 3*(self.prefix + self._expand_tribits(light_pt1, ZERO='100', ONE='110')) + \
                  2*(self.prefix+self._expand_tribits(light_pt2, ZERO='100', ONE='110'))  
        self._send(bin_seq, dongle)

    def turn_light_off(self, dongle):
        self.toggle_light(dongle)

    def turn_light_on(self, dongle):
        self.toggle_light(dongle)

    def set_fan_low(self, dongle):
        fanlow = self.code + '10000000000101111111111010'
        bin_seq = 4*(self.prefix + self._expand_tribits(fanlow, ZERO='100', ONE='110'))
        self._send(bin_seq, dongle)

    def set_fan_medium(self, dongle):
        fanmed = self.code + '10000001000001111110111110'
        bin_seq = 4*(self.prefix + self._expand_tribits(fanmed, ZERO='100', ONE='110'))
        self._send(bin_seq, dongle)

    def set_fan_high(self, dongle):
        fanhigh = self.code + '10000010000001111101111110'
        bin_seq = 4*(self.prefix + self._expand_tribits(fanhigh, ZERO='100', ONE='110'))
        self._send(bin_seq, dongle)

    def turn_fan_off(self, dongle):
        fanoff_pt1 = self.code + '10000000000011111111111100'
        fanoff_pt2 = self.code + '10000001000101111110111010'
        bin_seq = 3*(self.prefix + self._expand_tribits(fanoff_pt1, ZERO='100', ONE='110')) + 2*(self.prefix + self._expand_tribits(fanoff_pt2, ZERO='100', ONE='110'))
        self._send(bin_seq, dongle)


class Bedroom2FanLight(HunterFanLight):
    def __init__(self):
        super(Bedroom2FanLight, self).__init__()
        self.code = '11010001 11100011 00000011 01010100 10100000'.replace(" ", "")


class Bedroom1FanLight(HunterFanLight):
    def __init__(self):
        super(Bedroom1FanLight, self).__init__()
        self.code = '10111001 00110101 11101110 11011101 01000011'.replace(" ", "")

