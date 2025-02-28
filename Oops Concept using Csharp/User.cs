using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Oops_Concept
{
    class User
    {
        public string Username { get; set; }
        public string Role { get; protected set; }

        public virtual void AccessControl()
        {
            Console.WriteLine("Access control not defined.");
        }
    }

    // Admin class with full access
    class Admin : User
    {
        public Admin()
        {
            Role = "Admin";
        }

        public override void AccessControl()
        {
            Console.WriteLine("Admin Access: Full access to all system features.");
        }
    }

    // Customer class with limited access
    class Customer : User
    {
        public Customer()
        {
            Role = "Customer";
        }

        public override void AccessControl()
        {
            Console.WriteLine("Customer Access: Limited access to basic features.");
        }
    }
}
