using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Inheritance_with_Csharp
{
    public class Vehicle
    {
        public string? Brand { get; set; }
        public int Speed { get; set; }
    }
    public class Car : Vehicle
    {
        public void DisplayInfo()
        {
            Console.WriteLine($"Brand: {Brand}, Speed: {Speed} in KM/HR");
        }
    }
    public class Bike : Vehicle
    {
        public void DisplayInfo()
        {
            Console.WriteLine($"Brand: {Brand}, Speed: {Speed} in KM/HR");
        }
    }

}
