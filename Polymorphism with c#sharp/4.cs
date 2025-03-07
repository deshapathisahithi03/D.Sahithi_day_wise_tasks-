//How does Method Overriding work in C#? Demonstrate with Code and Explain the `override`, `virtual`, and `new` Keywords.
//Method overriding is a feature that allows a subclass to provide a specific implementation of a method that is already defined in its superclass.
//This allows the subclass to provide its own implementation of the method, which will be used instead of the superclass's implementation
//when the method is called on an instance of the subclass.
//The `override` keyword is used in the subclass to indicate that the method is overriding a method in the superclass. This keyword is used to
//provide the specific implementation of the method in the subclass.
//The `virtual` keyword is used in the superclass to indicate that the method can be overridden in a subclass. This keyword is used to define
//a method that can be overridden in a subclass, allowing for polymorphic behavior.
//The `new` keyword is used in the subclass to indicate that the method is hiding a method in the superclass. This keyword is used to provide
//a new implementation of a method in the subclass that is not related to the method in the superclass.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Polymorphism_with_c_sharp
{
    public class Method_Overriding
    {
        public virtual void student()
        {
            Console.WriteLine("I am A Student");
        }
        public virtual void student2()
        {
            Console.WriteLine("I am a Student 2");
        }
    }
        public class StudentDetails : Method_Overriding
        {
            public override void student()
            {
                base.student();
                Console.WriteLine("I am a college student studying Computer Science.");
            }

            public new void student2()
            {
                Console.WriteLine("I AM STUDENT OF Cse");


            }

        }
    }


