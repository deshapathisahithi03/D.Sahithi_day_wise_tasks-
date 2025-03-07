//What happens if a Base Class method is not marked as `virtual` but a Derived Class defines a method with the same name? Explain with an Example.
//Virtual methods are methods in a base class that can be overridden in derived classes. If a base class method is not marked as virtual,
//it cannot be overridden in derived classes. If a derived class defines a method with the same name as a non-virtual method in the base class,
//it is treated as a new method in the derived class and does not override the base class method.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Polymorphism_with_c_sharp
{
    public class BaseClass
    {
        public void Display()
        {
            Console.WriteLine("Base Class Display Method");
        }
    }
    public class ChildClass : BaseClass
    {
        public new void Display()
        {
            Console.WriteLine("Child Class Display Method");
        }
    }
}
    


