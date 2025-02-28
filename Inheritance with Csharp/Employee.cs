using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Inheritance_with_Csharp
{
    public class Employee
    {
        public string? Name { get; set; }
        public int Salary { get; set; }
        public Employee(string name, int salary) {
            Name = name;
            Salary = salary;
        }
    }
    public class Manager : Employee
    {
        public void DisplayInfo()
        {
            Console.WriteLine($"Name: {Name}, Salary: {Salary}");
        }
        public int Bonus { get; set; }

        public Manager(string name, int salary, int bonus) : base(name, salary)
        {
            Bonus = bonus;
        }
        public void DisplayInfo2()
        {
            Console.WriteLine($"Name: {Name}, Salary: {Salary}, Bonus: {Bonus}");
        }
    }
}
