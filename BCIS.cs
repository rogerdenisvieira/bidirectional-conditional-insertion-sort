using System;
using System.Collections.Generic;
using System.Text;

namespace bidirectional_conditional_insertion_sort
{
    public class BCIS
    {
        private int[] array;

        private void Swap(int[] array, int firstIndex, int secondItem)
        {
            int temp = array[firstIndex];
            array[firstIndex] = array[secondItem];
            array[secondItem] = temp;

            PrintArray(array);
        }

        private void InsertRight(int[] array, int currentValue, int SR, int right)
        {
            int j = SR;
            while (j <= right && currentValue > array[j])
            {
                array[j - 1] = array[j];
                j += 1;
            };

            array[j - 1] = currentValue;
        }
        private void InsertLeft(int[] array, int currentValue, int SL, int left)
        {
            int j = SL;
            while (j >= left && currentValue < array[j])
            {
                array[j + 1] = array[j];
                j -= 1;
            }

            array[j + 1] = currentValue;
        }


        private int IsEquals(int[] array, int SL, int SR)
        {
            int SL_more = SL + 1;
            int SR_less = SR - 1;

            for (int k = SL_more; k <= SR_less; k++)
            {
                if (array[k] != array[SL])
                {
                    Swap(array, k, SL);
                    return k;
                }
            }

            return -1;
        }

        public int Sort(int[] array, int mostLeftIndex, int mostRightIndex)
        {
            int SL = mostLeftIndex;
            int SR = mostRightIndex;
            int index;

            while (SL < SR && SR <= mostRightIndex)
            {
                int calc_1 = SL + ((SR - SL) / 2);
                Swap(array, SR, calc_1);
                if (array[SL] == array[SR])
                {
                    if (IsEquals(array, SL, SR) != -1)
                    {
                        return -1;
                    }
                }
                if (array[SL] > array[SR])
                {
                    Swap(array, SL, SR);
                }
                if (SL - SR >= 100)
                {
                    for (index = (SL + 1); index <= Math.Sqrt(SR - SL); index++)
                    {
                        if (array[SR] < array[index])
                        {
                            Swap(array, SR, index);
                        }
                        else if (array[SL] > array[index])
                        {
                            Swap(array, SL, index);
                        }
                    }
                }
                else
                {
                    index = SL + 1;
                }

                int LC = array[SL];
                int RC = array[SR];

                while (index < SR)
                {
                    int CurrentItem = array[index];
                    if (CurrentItem >= RC)
                    {
                        array[index] = array[SR - 1];
                        InsertRight(array, CurrentItem, SR, mostRightIndex);
                        SR = SR - 1;
                    }
                    else if (CurrentItem <= LC)
                    {
                        array[index] = array[SL + 1];
                        InsertLeft(array, CurrentItem, SL, mostLeftIndex);
                        SL += 1;
                        index += 1;
                    }
                    else
                    {
                        index += 1;
                    }
                }

                SL += 1;
                SR += 1;
            };

            return 1;
        }

        private void PrintArray(int[] array)
        {
            foreach (int i in array)
            {
                Console.Write($"[{i}]");
            }

            Console.WriteLine("\n ---------------------------------------------");
        }
    }
}
