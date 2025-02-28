using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Inheritance_with_Csharp
{
    public sealed  class SecuritySystem
    {
           public void AuthenticateUser()
        {
            Console.WriteLine("Authenticating user");
        }
    }
    public class Bank : SecuritySystem
    {
        public void DoBanking()
        {
            Console.WriteLine("Banking operations");
        }
    }
}
