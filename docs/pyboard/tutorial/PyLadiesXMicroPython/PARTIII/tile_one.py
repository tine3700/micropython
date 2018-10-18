from micropython import const
import pyb
from pyb import Pin
import machine

HDC_ADDR = const(64)
OPT_ADDR = const(69)

class TILE_ONE:

    def __init__(self, slot='X'):
        if (slot != 'X') and (slot != 'Y'):
            raise ValueError('either "X" or "Y" slot')
        i2c = machine.I2C(slot)

        self.buz_en = pyb.Pin(slot+'1', mode=pyb.Pin.OUT_PP, value=0)
        self.buz = Pin(slot+'6')

        leds = []
        for i in range(2, 5):
            leds.append(pyb.Pin(slot+'%d' % i, mode=Pin.OUT_OD, value=1))
        self.leds = leds

        self.opt_int = pyb.Pin(slot+'12', mode=Pin.OUT_OD, pull=Pin.PULL_UP, value=1)
        self.hdc_int = pyb.Pin(slot+'8', mode=Pin.OUT_OD, pull=Pin.PULL_UP, value=1)

        try:
            i2c.writeto_mem(OPT_ADDR, 0x1, b'\xcc\x10')   # continous mode, 800ms
            i2c.writeto_mem(HDC_ADDR, 0x0e, b'\x75')   # 5Hz, heater off, int act low, comp mode
            i2c.writeto_mem(HDC_ADDR, 0x0f, b'\x01')   # start
        except:
            pass

        self.i2c = i2c

        if slot == 'X':
            self.tim = 2
            self.chan = 1
        else:
            self.tim = 1
            self.chan = 1
        self.slot = slot

    def opt(self):
        man = self.i2c.readfrom_mem(OPT_ADDR, 0x7e, 2)
        dev = self.i2c.readfrom_mem(OPT_ADDR, 0x7f, 2)
        res = self.i2c.readfrom_mem(OPT_ADDR, 0x0, 2)
        res = (res[0] << 8) + res[1]
        exp = res >> 12
        res &= 0xfff
        res <<= exp
        return '%c%c%04x %.2f lux' % (man[0], man[1], (dev[0] << 8) + dev[1], res/100)
    
    def hdc(self):
        man = self.i2c.readfrom_mem(HDC_ADDR, 0xfc, 2)
        dev = self.i2c.readfrom_mem(HDC_ADDR, 0xfe, 2)
        temp = self.i2c.readfrom_mem(HDC_ADDR, 0x00, 2)
        hum = self.i2c.readfrom_mem(HDC_ADDR, 0x02, 2)
        temp = temp[0] + (temp[1] << 8)
        temp = temp*165/0x10000 - 40
        hum = hum[0] + (hum[1] << 8)
        hum = hum/0x10000*100
        return '%c%c%04x %.1f C %.1f %%' % (man[1], man[0], (dev[1] << 8) + dev[0], temp, hum)

    def heater(on=None):
        cfg = bytearray(2)
        if on is None:
            self.i2c.readfrom_mem_into(HDC_ADDR, 0x0e, cfg)
            return (cfg[0] & 8) > 0
        else:
            self.i2c.readfrom_mem_into(HDC_ADDR, 0x0e, cfg)
            if on:
                cfg[0] |= 8
            else:
                cfg[0] &= 0xf7
            self.i2c.writeto_mem(HDC_ADDR, 0x0e, cfg[:1])   # 5Hz, heater off, int act low, comp mode
            return on

    def beep(self, freq=4000, dur=100, v=100):
        if freq < 100:
            self.buz_en(0)
            return
        else:
            self.buz_en(1)
        if v < 1:
            v = 1
        elif v > 10:
            v = 10
            t = pyb.Timer(self.tim, freq=freq, mode=pyb.Timer.CENTER)
            t.channel(self.chan, pyb.Timer.PWM, pin=self.buz, pulse_width=(t.period() + 1) // (200//v))
            pyb.delay(dur)
            t.channel(self.chan, pyb.Timer.PWM, pin=self.buz, pulse_width=0)
            #self.buz_en(0)

    def led(self, color):
        color ^= 7
        self.leds[0](color & 1)
        self.leds[1](color & 2)
        self.leds[2](color & 4)

    def demo(self, n=0, dt=1000, rgb=0):
        i = rgb
        t0 = pyb.millis()
        next = t0
        while True:
            hdc = self.hdc()
            lux = self.opt()
            self.beep(dur=150)
            self.beep(0)
            self.led(i & 7)
            print(next, i, hdc, lux)
            t0 = pyb.millis()
            i += 1
            pyb.delay(next-t0)
            next += dt
            if n == 0:
                break
            elif n > 0:
                n -= 1
        
    

