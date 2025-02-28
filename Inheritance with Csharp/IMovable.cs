using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Inheritance_with_Csharp
{
    public interface IMovable
    {
        public void Move();
    }

    public class Machine
    {
        public void start()
        {
            Console.WriteLine("Machine is starting");
        }
    }
    public class Robot : Machine, IMovable
    {


        public void Move()
        {
            Console.WriteLine("Robot is moving");
        }
    }
}
