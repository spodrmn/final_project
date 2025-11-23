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

        # validity check

        if not (0 <= i < w) or not (0 <= j < h):
            raise IndexError

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
        
        w = self._width
        h = self._height

        # c = minimum energy

        c = {}

        # p = parents

        p = {}

        #base case

        for x in range(w): 
            c[(x,0)] = self.energy(x,0)
            p[(x,0)] = None

        #recursive cases

        for y in range(1,h):
            for x in range(w):

                parents = []

                #append the pixel directly above

                parents.append((x,y-1))

                #append the pixel above and to the left if it's greater than zero

                if x > 0:
                    parents.append((x-1, y-1))

                #append the one up and to the right if it's less than the width-1

                if x < w-1: 
                    parents.append((x+1, y-1))

                #choose pixel with minimal energy

                selected_p = min(parents,key = lambda coord: c[coord])

                #update 

                c[(x,y)] = self.energy(x,y) + c[selected_p] #stores the energy
                p[(x,y)] = selected_p[0]                    # stores the x coordinate only
                
        #find the end of the seam
        seam_end = min(range(w), key = lambda x: c[(x,h-1)])

        #add end to end of list

        seam = [0]*h
        seam[h-1] = seam_end

        x = seam_end
        for y in range(h -1,0, -1):
            x = p[(x,y)]
            seam[y-1] = x

        return seam


    def find_horizontal_seam(self) -> list[int]:
        '''
        Return a sequence of indices representing the lowest-energy
        horizontal seam
        '''
        w = self._width
        h = self._height

        # c = minimum energy

        c = {}

        # p = parents

        p = {}

        #base case

        for y in range(h): 
            c[(0,y)] = self.energy(0,y)
            p[(0,y)] = None

        #recursive cases

        for x in range(1,w):
            for y in range(h):

                parents = []

                #append the pixel directly to the left

                parents.append((x-1,y))

                #append the pixel to the left and above if it's greater than zero

                if y > 0:
                    parents.append((x-1, y-1))

                #append the one to the left and below if it's less than the height-1

                if y < h-1: 
                    parents.append((x-1, y+1))

                #choose pixel with minimal energy

                selected_p = min(parents,key = lambda coord: c[coord])

                #update 

                c[(x,y)] = self.energy(x,y) + c[selected_p] #stores the energy
                p[(x,y)] = selected_p[1]                    # stores the y coordinate only

                
        #find the end of the seam
        seam_end = min(range(h), key = lambda y: c[(w-1,y)])

        #add end to end of list

        seam = [0]*w
        seam[w-1] = seam_end

        y = seam_end
        for x in range(w -1,0, -1):
            y = p[(x,y)]
            seam[x-1] = y

        return seam

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
