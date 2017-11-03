"""
File: fileFinder.py
Author(s): Tom Daniels
Purpose: Finds and attempts to recover a deleted file in the NTFS file system
"""
################################################################################
#                                                                              #
#                            Imports and Definitions                           #
#                                                                              #
################################################################################
import ctypes, os, sys
from io_helper import *

SECTOR_SIZE=512    # Assume the size of a sector is 512 bytes
CLUSTER_SIZE=8     # Assume the size of a cluster is 8 sectors
SECTOR_OFFSET=11   # Offset that tells us # of bytes per sector. 2 bytes
CLUSTER_OFFSET=13  # Offset that tells us # of sectors per cluster. 1 byte
MTF_OFFSET=48      # Offset that tells us which cluster MTF starts at. 8 bytes

################################################################################
#                                                                              #
#                                   Functions                                  #
#                                                                              #
################################################################################
def getMFTStartIndex():
    """
    Purpose: Gets the offset of the MFT in bytes
    @return  (int) Offset of the MFT in bytes
    """
    bootSector = read_image(0, SECTOR_SIZE) # Read 1st disk sector

    # Redefine SECTOR_SIZE or CLUSTER_SIZE if they're different than expected
    SECTOR_SIZE = int(convertToHex(bootSector[SECTOR_OFFSET:CLUSTER_OFFSET]), 16)
    CLUSTER_SIZE = int(convertToHex(bootSector[CLUSTER_OFFSET]), 16)

    # Return the offset of the MFT in bytes. The boot sector holds the MFT
    # offset in terms of clusters, so convert clusters to bytes
    return SECTOR_SIZE*CLUSTER_SIZE*int(convertToHex(bootSector[MTF_OFFSET:MTF_OFFSET+8]), 16)

def main():
    # Get offset in number of bytes
    MTFStartIndex = getMFTStartIndex()

if(__name__ == '__main__'):
    if(not ctypes.windll.shell32.IsUserAnAdmin()):
        print("Error, you must be an administrator to use this program")
        sys.exit()
    main()
