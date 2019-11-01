import math
#import matplotlib.pyplot as plt

class BCIS:

    def __print_array(self, array):
        for i in array:
            print("{0}".format(i), end =" ")        
        print("")

    
    def __swap(self, array, first_index, second_index):
        temp = array[first_index]
        array[first_index] = array[second_index]
        array[second_index] = temp


    def __insert_right(self, array, current_item, sr, right):
        j = sr
        while(j <= right and current_item > array[j]):
            array[j - 1] = array[j]
            j +=1

        array[j - 1] = current_item


    def __insert_left(self, array, current_item, sl, left):
        j = sl
        while(j >= left and current_item < array[j]):
            array[j+1] = array[j]
            j -=1

        array[j + 1] = current_item


    def __is_equals(self, array, sl_index, sr_index):
        sl_more = sl_index + 1
        sr_less = sr_index - 1

        for k in range(sl_more, sr_less):
            if(array[k] != array[sl_index]):
                self.__swap(array, k, sl_index)
                return k
        return -1

    def sort(self, array, sl_index, sr_index):
        sl = sl_index
        sr = sr_index

        while(sl < sr and sr <= sr_index):
            calc_1= sl + ((sr - sl)//2)
            self.__swap(array, sr, calc_1)

            if(array[sl] == array[sr]):
                if(self.__is_equals(array, sl, sr) != -1):
                    return -1
            
            if(array[sl] > array[sr]):
                self.__swap(array, sl, sr)

            if(sl - sr >= 100):
                for i in range((sl + 1), math.sqrt(sr - sl)):
                    if(array[sr] < array[i]):
                        self.__swap(array, sr, i)
                    elif(array[sl] > array[i]):
                        self.__swap(array, sl, i)
            else:
                i = sl + 1

            lc = array[sl]
            rc = array[sr]

            while(i < sr):
                current_item = array[i]

                if(current_item >= rc):
                    array[i] = array[sr - 1]
                    self.__insert_right(array, current_item, sr, sr_index)
                    sr = sr - 1

                elif(current_item <= lc):
                    array[i] = array[sl + 1]
                    self.__insert_left(array, current_item, sl, sl_index)
                    sl += 1
                    i += 1
                else:
                    i += 1
            sl += 1
            sr += 1
        return 1

class QS:

    # Python program for implementation of Quicksort Sort 

    # This function takes last element as pivot, places 
    # the pivot element at its correct position in sorted 
    # array, and places all smaller (smaller than pivot) 
    # to left of pivot and all greater elements to right 
    # of pivot 
    def __partition(self,arr,low,high): 
        i = ( low-1 )		 # index of smaller element 
        pivot = arr[high]	 # pivot 

        for j in range(low , high): 

            # If current element is smaller than or 
            # equal to pivot 
            if arr[j] <= pivot: 
            
                # increment index of smaller element 
                i = i+1
                arr[i],arr[j] = arr[j],arr[i] 

        arr[i+1],arr[high] = arr[high],arr[i+1] 
        return ( i+1 ) 

    # The main function that implements QuickSort 
    # arr[] --> Array to be sorted, 
    # low --> Starting index, 
    # high --> Ending index 

    # Function to do Quick sort 
    def sort(self,arr,low,high): 
        if low < high: 

            # pi is partitioning index, arr[p] is now 
            # at right place 
            pi = self.__partition(arr,low,high) 

            # Separately sort elements before 
            # partition and after partition 
            self.sort(arr, low, pi-1) 
            self.sort(arr, pi+1, high) 





