using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace Oops_Concept
{
    public class Vehicle
    {
        public virtual void start()
        {
            Console.WriteLine("the vehicle is starting");
        }


    }
    public class Car : Vehicle
    {

        public override void start()
        {

            Console.WriteLine("the car is starting");

        }

    }
    public class Bike : Vehicle
    {
        public override void start()
        {
            Console.WriteLine("bike is starting");
        }
    }
}

