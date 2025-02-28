using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Oops_Concept
{
    public class Person
    {
            public string Name { get; set; }
            public int Age { get; set; }

            public virtual void GetDetails()
            {
                Console.WriteLine($"Name: {Name}, Age: {Age}");
            }
        }

        class Student : Person
        {
            public string StudentID { get; set; }

            public override void GetDetails()
            {
                Console.WriteLine($"Student: {Name}, Age: {Age}, ID: {StudentID}");
            }
        }

        class Teacher : Person
        {
            public string Subject { get; set; }

            public override void GetDetails()
            {
                Console.WriteLine($"Teacher: {Name}, Age: {Age}, Subject: {Subject}");
            }
        }
    }
