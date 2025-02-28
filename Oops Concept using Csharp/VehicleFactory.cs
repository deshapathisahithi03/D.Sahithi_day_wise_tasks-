using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Oops_Concept
{
        public interface IVehicle
        {
            void Drive();
        }

        // Concrete Car class
        public class Cars : IVehicle
        {
            public void Drive()
            {
                Console.WriteLine("Car is driving...");
            }
        }

        // Concrete Bike class
        public class Bikes : IVehicle
        {
            public void Drive()
            {
                Console.WriteLine("Bike is riding...");
            }
        }

        // Factory class
        public class VehicleFactory
        {
            // Factory Method
            public static IVehicle GetVehicle(string vehicleType)
            {
                switch (vehicleType.ToLower())
                {
                    case "car":
                        return new Cars();
                    case "bike":
                        return new Bikes();
                    default:
                        throw new ArgumentException("Invalid vehicle type.");
                }
            }
        }
}
