# Functions for reading and writing bytes on a hard drive.

import os

def read_image(offset, size):

    # Builds the string specifying the primary parition's file path.
    systemDrive = '\\\\.\\' + os.getenv('SystemDrive')

    # Opens the primary partition, seeks to a offset, and then
    # returns the amout of bytes specified by the size parameter.
    image = open(systemDrive, 'rb')
    image.seek(offset)

    return image.read(size)



