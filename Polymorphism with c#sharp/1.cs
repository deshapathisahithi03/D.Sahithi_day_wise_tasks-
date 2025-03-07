//1.	1. Explain Polymorphism in C# with a Real-World Example.

//Polymorphism is a concept in object-oriented programming that allows objects to be treated as instances of their parent class. This means that
//a parent class can be used to create objects of its child classes, and these objects can be used interchangeably with objects of the parent
//class. Polymorphism allows for flexibility and extensibility in object-oriented design, as it enables code to be written in a way that is
//more generic and reusable.



using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Polymorphism_with_c_sharp
{
    public class FoodDelivery_App
    {
        public virtual void Delivery()
        {
            Console.WriteLine("Food is delivered to the customer");
        }

    }

    public class Zomato : FoodDelivery_App
    {
        public override void Delivery()
        {
            Console.WriteLine("Food is delivered to the customer by Zomato and Received Cash back Point");
        }
        public void Rating(int rating)
        {
            Console.WriteLine($" Rating given to the food in Zomato is {rating}/10");
        }
    }
    public class Swiggy : FoodDelivery_App
    {
        public override void Delivery()
        {
            Console.WriteLine("Food is delivered to the customer by Swiggy and Received Coupon for movie Tickets");
        }
        public void Rating(int rating)
        {
            Console.WriteLine($" Rating given to the food in Swiggy is {rating}/10");
        }
    }

}
