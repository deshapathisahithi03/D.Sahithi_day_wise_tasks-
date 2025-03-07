using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Polymorphism_with_c_sharp
{
    class Animals
    {
        public virtual void Speak()
        {
            Console.WriteLine("Animal speaks");
        }
    }

    class Dogs : Animals
    {
        public override void Speak()
        {
            Console.WriteLine("Dog barks");
        }
    }

}
