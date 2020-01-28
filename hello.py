#!/usr/bin/env python

'''Hello Farmware Test

A simple Farmware example that tells FarmBot to log a new message including the provided input.
'''

from farmware_tools import get_config_value, device

INPUT_VALUE = get_config_value(
    farmware_name='Hello Farmware Test', config_name='input', value_type=str)
device.log(message='Hello Farmware! Test input was: {}'.format(
    INPUT_VALUE), message_type='success')
device.log(message="Message 1 Test", message_type="success")
device.log(message="Message 2 Test", message_type="success")
device.log(message="Message 3 Test", message_type="success")
device.log(message="Message 4 Test", message_type="success")
device.log(message="Message 5 Test", message_type="success")
zero = device.assemble_coordinate(0, 0, 0)
one = device.assemble_coordinate(10, 10, 0)
two = device.assemble_coordinate(20, 20, 0)
three = device.assemble_coordinate(30, 30, 0)
four = device.assemble_coordinate(40, 40, 0)
five = device.assemble_coordinate(50, 50, 0)

device.move_absolute(one, 100, zero)

device.move_absolute(two, 100, zero)

device.move_absolute(three, 100, zero)

device.move_absolute(four, 100, zero)

device.move_absolute(five, 100, zero)
