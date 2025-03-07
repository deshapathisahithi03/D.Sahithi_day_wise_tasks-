using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Polymorphism_with_c_sharp
{
    public class Overriding
    {
        public virtual void show()
        {
            Console.WriteLine("The movie is about to start");
        }
    }
    public class Movie1 : Overriding {
        public override void show()
        {
            Console.WriteLine("The movie is about to start and I am Very Excited");
        }
        public void movie(string name)
        {
              Console.WriteLine($"The movie is about to start and the movie is {name}");
        }

    }
}
