using System.Diagnostics.Tracing;

namespace execpetion
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");

            try
            {
                Console.WriteLine("Enter a number");
                int a = Convert.ToInt32(Console.ReadLine());
                int n = 0;
                n = a / n;
                Console.WriteLine("a is" + a);
                string name = "Hello";
                name.Substring(10, 10);
                checked
                {
                    n = n + 10;
                }


            }
            catch (NullReferenceException e)
            {
                Console.WriteLine("Error: The number is null");
            }

            catch (FormatException e)
            {
                Console.WriteLine("Error: The number is not in the correct format");
            }
            catch (ArgumentOutOfRangeException e)
            {
                Console.WriteLine("Error: The number is out of range");
            }
            catch (DivideByZeroException e)
            {
                Console.WriteLine("Error: The number Cannot be divided by zero ");
            }

            catch (Exception e)
            {
                Console.WriteLine("Error: " + e.Message);
            }
            finally//memory cleanup
            {
                Console.WriteLine("Finally block is executed");
            }
        }
    }
}
