
//*******Explain how Interfaces and Abstract Classes enable Polymorphism. When should you use one over the other?
//Interfaces and Abstract Classes are two ways to enable polymorphism in C#. Both interfaces and abstract classes allow you to define
//a contract that a class must implement, but they do so in different ways.
//An interface is a contract that defines a set of methods and properties that a class must implement. An interface does not provide any
//implementation for these methods and properties, but it defines the signature that the implementing class must follow. An interface
//allows a class to implement multiple interfaces, enabling it to have multiple types.
//An abstract class is a class that cannot be instantiated on its own, but it can be used as a base class for other classes. An abstract
//class can define abstract methods and properties that must be implemented by the subclass. An abstract class can also provide
//implementation for some methods and properties, allowing the subclass to override
//only the methods and properties that are necessary.
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Polymorphism_with_c_sharp
{
    public interface IShape
    {
        void Area();

    }
    
    public class Rectangle : IShape
    {
        private double Length { get; set; }
        private double Bredth { get; set; }
        public Rectangle(double length, double bredth)
        {
            Length = length;
            Bredth = bredth;
        }

      public void Area()
        {
            Console.WriteLine($"The area of THE Rectangle is:{Length * Bredth}");
        }
    }
}
