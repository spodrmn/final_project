#!/usr/bin/env python3

from picture import Picture
import math

class SeamCarver(Picture):
    ## TO-DO: fill in the methods below
    def energy(self, i: int, j: int) -> float:
        '''
        Return the energy of pixel at column i and row j

        '''
        w = self._width
        h = self._height

        #neighbor indexes with wraparounds

        left = (i-1) % w
        right = (i+1) % w
        up = (j-1) % h
        down = (j+1) % h

        #neighbor pixels 

        left_pixel = self[left, j]
        right_pixel = self[right, j]
        up_pixel = self[i, up]
        down_pixel = self[i, down]

        # x-gradient
        Rx = abs(left_pixel[0]-right_pixel[0])
        Gx = abs(left_pixel[1]-right_pixel[1])
        Bx = abs(left_pixel[2]-right_pixel[2])

        # y-gradient
        Ry = abs(up_pixel[0]-down_pixel[0])
        Gy = abs(up_pixel[1]-down_pixel[1])
        By = abs(up_pixel[2]-down_pixel[2])

        energy = math.sqrt(Rx**2 + Gx**2 + Bx**2 + Ry**2 + Gy**2 + By**2)

        return energy
    

    def find_vertical_seam(self) -> list[int]:
        '''
        Return a sequence of indices representing the lowest-energy
        vertical seam
        '''
        raise NotImplementedError

    def find_horizontal_seam(self) -> list[int]:
        '''
        Return a sequence of indices representing the lowest-energy
        horizontal seam
        '''
        raise NotImplementedError

    def remove_vertical_seam(self, seam: list[int]):
        '''
        Remove a vertical seam from the picture
        '''
        raise NotImplementedError

    def remove_horizontal_seam(self, seam: list[int]):
        '''
        Remove a horizontal seam from the picture
        '''
        raise NotImplementedError

class SeamError(Exception):
    pass
