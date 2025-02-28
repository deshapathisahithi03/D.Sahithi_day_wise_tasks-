using System;
using System.Collections.Generic;
using System.Diagnostics.Contracts;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Oops_Concept
{
    public abstract class Shape
    {
        public abstract double CalculateArea();
    }
    public class Circle : Shape
    {
        public double Radius { get; set; }
        public Circle(double radius)
        {
            Radius = radius;
        }
        public override double CalculateArea()
        {
            return Math.PI * Math.Pow(Radius, 2);
        }
    }
    public class Rectangle : Shape
    {
        public double Length { get; set; }
        public double Breadth { get; set; }
        public Rectangle(double length, double breadth)
        {
            Length = length;
            Breadth = breadth;
        }
        public override double CalculateArea()
        {
            return Length * Breadth;
        }
    }
}
