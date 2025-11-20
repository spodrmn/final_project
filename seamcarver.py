#!/usr/bin/env python3

from picture import Picture
import math

class SeamCarver(Picture):
    ## TO-DO: fill in the methods below
    def energy(self, i: int, j: int) -> float:
        '''
        Return the energy of pixel at column i and row j

        '''
        if i == 0: 
            Rx = abs(self[self._width-1, j][0] - self[i+1, j][0])
            Gx = abs(self[self._width-1, j][1] - self[i+1, j][1])
            Bx = abs(self[self._width-1, j][2] - self[i+1, j][2])

        elif i == self._width-1: 
            Rx = abs(self[i-1, j][0] - self[0, j][0])
            Gx = abs(self[i-1, j][1] - self[0, j][1])
            Bx = abs(self[i-1, j][2] - self[0, j][2])       

        else: 
            Rx = abs(self[i-1, j][0] - self[i+1, j][0])
            Gx = abs(self[i-1, j][1] - self[i+1, j][1])
            Bx = abs(self[i-1, j][2] - self[i+1, j][2])

        if j ==0:
            Ry = abs(self[i, j+1][0] - self[i, self._height-1][0])
            Gy = abs(self[i, j+1][1] - self[i, self._height-1][1])
            By = abs(self[i, j+1][2] - self[i, self._height-1][2])            

        elif j== self._height-1:
            Ry = abs(self[i, 0][0] - self[i, j-1][0])
            Gy = abs(self[i, 0][1] - self[i, j-1][1])
            By = abs(self[i, 0][2] - self[i, j-1][2])

        else: 
            Ry = abs(self[i, j+1][0] - self[i, j-1][0])
            Gy = abs(self[i, j+1][1] - self[i, j-1][1])
            By = abs(self[i, j+1][2] - self[i, j-1][2])

        energy = math.sqrt(Rx**2 + Gx**2 + Bx**2 + Ry**2 + Gy**2 + By**2)

        return energy

        raise NotImplementedError
    

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
