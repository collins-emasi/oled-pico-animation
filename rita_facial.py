import os
import framebuf
from utime import sleep
from random import choice

from SSD1306LIB import SSD1306_I2C

class RitaFacial:
    def __init__(self, OLED : SSD1306_I2C, inversion : int = 1) -> None:
        self.expression_files = []
        self.OLED = OLED
        self.inversion = inversion
        self.expressions = ['blink', 'smile']

    def get_expression_files(self, expression : str) -> None:
        """
        Curates all the files for the expression desired
        and then sorts the list
        """
        files = os.listdir("/")
        self.expression_files = [file for file in files if file.startswith(expression)]
        self.expression_files.sort()

    def express(self, expression : str) -> None:
        """
        Expresses any of the list of expressions 
        Listed in the self.expressions in the init
        function
        """
        assert(expression in self.expressions)

        self.get_expression_files(expression)
        images = []
        
        for n in range(len(self.expression_files)):
            with open(self.expression_files[n], 'rb') as f:
                for _ in range(3):
                    f.readline()
                data = bytearray(f.read())
            fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)
            images.append(fbuf)
        
        def show_procedure(image, time_ms : int | float):
            self.OLED.invert(self.inversion)
            self.OLED.blit(image, 0, 0)
            self.OLED.show()
            sleep(time_ms)
        
        for i in images:
            show_procedure(i, 0.005)

        sleep(0.05)

        for i in reversed(images):
            show_procedure(i, 0.005)

    def express_random(self):
        """
        This function expresses a random epression from the
        self.expression list
        """
        expression = choice(self.expressions)
        self.express(expression=expression)
    
