using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Inheritance_with_Csharp
{
    public class Person
    {
        public void Greet()
        {
            Console.WriteLine("Hello");
        }
    }
    public class Student : Person
    {
        public void Study()
        {
            Console.WriteLine("I'm studying");
        }
    }
}
