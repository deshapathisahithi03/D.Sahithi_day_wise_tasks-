using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

namespace Inheritance_with_Csharp
{
    public class Vehicle2
    {
        public string? Brand { get; set; }
        public int Speed { get; set; }

        public Vehicle2(string brand, int speed)
        {
            Brand = brand;
            Speed = speed;
        }
        public virtual void DisplayInfo()
        {
            Console.WriteLine($"Brand: {Brand}, Speed: {Speed} in KM/HR");
        }
    }
    public class Car2 : Vehicle2
    {
        public Car2(string brand, int speed) : base(brand, speed)
        {
        }
        public override void DisplayInfo()
        {
            Console.WriteLine($"Brand: {Brand}, Speed: {Speed} in KM/HR");
        }

        public void Homeadress(string address)
        {
            Console.WriteLine($"{address} is the home address of the car");
        }
    }
    public class Bike2 : Vehicle2
    {
        public Bike2(string brand, int speed) : base(brand, speed)
        {
        }
        public override void DisplayInfo()
        {
            Console.WriteLine($"Brand: {Brand}, Speed: {Speed} in KM/HR");
        }
        public void Homeaddress(string address)
        {

            Console.WriteLine($"{address} is the home address of the bike");
        }
    }
}
