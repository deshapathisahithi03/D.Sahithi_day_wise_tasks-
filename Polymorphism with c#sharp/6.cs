using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Polymorphism_with_c_sharp
{
    public abstract class Animal
    {
        public abstract void Display();
    }
    public class Dog : Animal
    {
        public override void Display()
        {
            Console.WriteLine("i am a Animal");
        }

    }
    public class Puppy:Dog
    {
        public override void Display()
        {
            Console.WriteLine("I am from Dog family");
        }
    }
}
