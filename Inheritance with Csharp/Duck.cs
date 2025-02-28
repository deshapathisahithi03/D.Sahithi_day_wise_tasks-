using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Inheritance_with_Csharp
{

    public interface IFlyable
    {
        public void Fly();
    }
    public interface ISwimmable
    {
        public void Swim();
    }
    public class Duck : IFlyable, ISwimmable
    {
        public void Fly()
        {
            Console.WriteLine("Duck can fly");
        }
        public void Swim()
        {
            Console.WriteLine("Duck can swimm");

        }
    }
}