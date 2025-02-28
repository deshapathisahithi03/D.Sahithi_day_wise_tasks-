using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Inheritance_with_Csharp
{
    public class Account
    {
        public virtual void CalculateInterest()
        {
            Console.WriteLine("Calculating interest for the account ");
        }
    }
    public class SavingsAccount : Account
    {
        public sealed override void CalculateInterest()
        {
            Console.WriteLine("Calculating interest for the savings account");
        }
    }
}
