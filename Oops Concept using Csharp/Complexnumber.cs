using System;

namespace Oops_Concept
{
    public class ComplexNumber // Fixed class name to match constructor
    {
        public double Real { get; set; }
        public double Imaginary { get; set; }

        // Constructor
        public ComplexNumber(double real, double imaginary)
        {
            Real = real;
            Imaginary = imaginary;
        }

        // Overloading the + operator
        public static ComplexNumber operator +(ComplexNumber c1, ComplexNumber c2)
        {
            return new ComplexNumber(c1.Real + c2.Real, c1.Imaginary + c2.Imaginary);
        }

        // Overriding ToString() for better output
        public override string ToString()
        {
            return $"{Real} + {Imaginary}i";
        }
    }
}
