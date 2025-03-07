//How does Polymorphism improve Code Maintainability and Extensibility? Provide a Scenario.
//Polymorphism improve Code Maintainability and Extensibility by allowing us to write code that is more flexible and easier to maintain.
//Polymorphism allows us to write code that can work with objects of different types, without having to know the specific type of each object.
//This makes our code more reusable and easier to extend, as we can add new types of objects without having to modify the existing code.
//For example, consider a Vehicle class that has a Display method. We can create a Car class that inherits from the Vehicle class and overrides
//the Display method to provide a specific implementation for cars. When we call the Display method on a Car object, the car-specific
//implementation will be executed. This allows us to write code that can work with any type of vehicle, without having to know the specific
//type of each vehicle. If we later add a Truck class that inherits from the Vehicle class and overrides the Display method, our existing
//code will still work with trucks without any modifications. This makes our code more maintainable and extensible, as we can easily
//add new types of vehicles without having to change the existing code.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Polymorphism_with_c_sharp
{
    public class Vehicle
    {
        public void Display()
        {
            Console.WriteLine("Vehicle Display Method");
        }
    }
    public class Car : Vehicle
    {
        public new void Display()
        {
            Console.WriteLine("Car Display Method");
        }
    }
}
