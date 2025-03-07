//How does Method Overloading work in C#? Provide an Example where it is useful.
//Method overloading is a feature that allows a class to have more than one method having the same name, if their argument lists are different.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Polymorphism_with_c_sharp
{
    class Method_Overloading
    {
        public void student()
        {
            Console.WriteLine("I am A Student");
        }

        public void student(string name)
        {
            Console.WriteLine($"Student name is {name}");
        }
        public void student(string name,string roll_no)
        {
            Console.WriteLine($"I am {name} bearing the rollno = {roll_no}");
        }
    }
}
