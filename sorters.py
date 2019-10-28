import math
#import matplotlib.pyplot as plt

class BCIS:

    def print_array(self, array):
        for i in array:
            print("{0}".format(i), end =" ")        
        print("")

    
    def swap(self, array, i, j):
        temp = array[i]
        array[i] = array[j]
        array[j] = temp

        # printing arrays's content
        self.print_array(array)

    def insert_right(self, array, current_item, sr, right):
        j = sr
        while(j <= right and current_item > array[j]):
            array[j - 1] = array[j]
            j +=1

        array[j - 1] = current_item


    def insert_left(self, array, current_item, sl, left):
        j = sl
        while(j >= left and current_item < array[j]):
            array[j+1] = array[j]
            j -=1

        array[j + 1] = current_item


    def is_equals(self, array, sl, sr):
        sl_more = sl + 1
        sr_less = sr - 1

        for k in range(sl_more, sr_less):
            if(array[k] != array[sl]):
                self.swap(array, k, sl)
                return k
        return -1

    def sort(self, array, left, right):
        sl = left
        sr = right

        while(sl < sr and sr <= right):
            calc_1= sl + ((sr - sl)//2)
            self.swap(array, sr, calc_1)

            if(array[sl] == array[sr]):
                if(self.is_equals(array, sl, sr) != -1):
                    return -1
            
            if(array[sl] > array[sr]):
                self.swap(array, sl, sr)

            if(sl - sr >= 100):
                rnge = range((sl + 1), math.sqrt(sr - sl))
                for i in range((sl + 1), math.sqrt(sr - sl)):
                    if(array[sr] < array[i]):
                        self.swap(array, sr, i)
                    elif(array[sl] > array[i]):
                        self.swap(array, sl, i)
            else:
                i = sl + 1

            lc = array[sl]
            rc = array[sr]

            while(i < sr):
                current_item = array[i]

                if(current_item >= rc):
                    array[i] = array[sr - 1]
                    self.insert_right(array, current_item, sr, right)
                    sr = sr - 1

                elif(current_item <= lc):
                    array[i] = array[sl + 1]
                    self.insert_left(array, current_item, sl, left)
                    sl += 1
                    i += 1
                else:
                    i += 1
            sl += 1
            sr += 1
        return 1





