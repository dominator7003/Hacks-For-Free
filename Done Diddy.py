import time
from Adafruit_IO import Client, Feed
import pyfirmata

run_count = 0

ADAFRUIT_IO_USERNAME = "aio_qrJW424cCjfYYISvfOBSCxTqrbif"
ADAFRUIT_IO_KEY = "aio_qrJW424cCjfYYISvfOBSCxTqrbif"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)


board = pyfirmata.Arduino('COM4')
it = pyfirmata.util.Iterator(board)
it.start()


digital_output = board.get_pin('d:2:o')
analogue_INPUT = board.get_pin('a:1:o')

try:
    digital = aio.feeds('digital')
    pot = aio.feeds('pot')
except:
    feed = Feed(name='digital')
    digital = aio.create_feed(feed)
    feed = Feed(name='pot')
    digital = aio.create_feed(feed)

while True:
    print('Sending count:', run_count)
    run_count += 1
    aio.send_data('counter', run_count)

    data = aio.receive(digital.key)
    print('Data:', data.value)
    pot = aio.receive(digital.key)
    print('pot:', data.value)

    if data.value == "ON":
        digital_output.write(True)
    else:
        digital_output.write(False)

    time.sleep(3)


while True:
    print('Sending count:', run_count)
    aio.send_data('counter', run_count)
    run_count += 1
    print('pot val:', run_count)
    aio.send_data('pot', run_count)

    time.sleep(5)
    
