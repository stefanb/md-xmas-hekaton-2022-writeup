using System;
					
public class Program
{
	public static double M()
    {
        int num = 34;
        int num2 = 6;
        double num3 = 2.5;
        double num4 = (double)num / (double)num2;
        if ((int)num4 >= num2)
        {
            return num2 * (int)num4;
        }
        return num ^ num2;
    }
	
	public static void Main()
	{
		Console.WriteLine(M());
	}
}