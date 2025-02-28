using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Inheritance_with_Csharp
{
    public class Product
    {
        public string Name { get; set; }
        public double Price { get; set; }

        public Product(string name, double price)
        {
            Name = name;
            Price = price;
        }

        // Virtual method to calculate discounted price
        public virtual double GetDiscountedPrice()
        {
            return Price; // No discount by default
        }

        public void DisplayInfo()
        {
            Console.WriteLine($"Product: {Name}, Price: ₹{Price:F2}, Discounted Price: ₹{GetDiscountedPrice():F2}");
        }
    }

    class ElectronicProduct : Product
    {
        public ElectronicProduct(string name, double price) : base(name, price) { }

        // Override to apply 10% discount
        public override double GetDiscountedPrice()
        {
            return Price * 0.90;
        }
    }

    class ClothingProduct : Product
    {
        public ClothingProduct(string name, double price) : base(name, price) { }

        // Override to apply 20% discount
        public override double GetDiscountedPrice()
        {
            return Price * 0.80;
        }

    }
}
