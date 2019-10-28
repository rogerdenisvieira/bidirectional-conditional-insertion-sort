using System;

namespace bidirectional_conditional_insertion_sort
{
    class Program
    {
        static void Main(string[] args)
        {
            BCIS bcisSorter = new BCIS();

            int[] array = CreateRandomIntArray(1000, 0, 200);

            bcisSorter.Sort(array, 0, array.Length - 1);
        }

        static int[] CreateRandomIntArray(int size, int minValue, int maxValue)
        {
            int[] array = new int[size];
            Random random = new Random();

            for (int i = 0; i < array.Length; i++)
            {
                array[i] = random.Next(minValue, maxValue);
            }
            
            return array;
        }
    }
}
