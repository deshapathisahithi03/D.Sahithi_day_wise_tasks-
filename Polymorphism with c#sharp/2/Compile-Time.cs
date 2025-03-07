using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Polymorphism_with_c_sharp
{
    public class Overloading
    {
        public void Delivery()
        {
            Console.WriteLine("Food is delivered to the customer");

        }
        public void Delivery(string name)
        {
            Console.WriteLine($"Food is delivered to the customer by {name}");
        }
        public void Delievery(string name, string item)
        {
            Console.WriteLine($"Food is delivered to the customer by {name} and the item is {item}");
        }
    }
}
