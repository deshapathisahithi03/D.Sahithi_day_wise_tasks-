using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Oops_Concept
{
    public class Calculator
    {
        // Overloaded Add method for two integers
        public int Add(int a, int b)
        {
            return a + b;
        }

        // Overloaded Add method for three integers
        public int Add(int a, int b, int c)
        {
            return a + b + c;
        }

        // Overloaded Add method for two double values
        public double Add(double a, double b)
        {
            return a + b;
        }
    }
}
