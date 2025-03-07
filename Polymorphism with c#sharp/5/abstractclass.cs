using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Polymorphism_with_c_sharp
{
   public  abstract class Shapes
    {
        public abstract void Area();

        public void Display()
        {
            Console.WriteLine("This is a Abstract class");
        }

    }
    public class Rectangles : Shapes
    {
    
        private double length;
        private double bredth;
        
        public Rectangles(double x, double y)
        {
            this.length = x;
            this.bredth = y;
        }

        public override void Area()
        {
            Console.WriteLine($"The Area of the Rectangle is{length * bredth}");

        }

    }
}
