using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Oops_Concept
{
    public class Students_Details
    {
        private string? name;
        private string? rollNo;

        public string? Name
        {
            get { return name; }
            set { 
                if (value!=null)
                {
                    name = value;
                }
                else
                {
                    Console.WriteLine("Name cannot be null");
                }
              }
        }
        public string? RollNo
        {
            get { return rollNo; }
            set
            {
                if (value != null)
                {
                    rollNo = value;
                }
                else
                {
                    Console.WriteLine("RollNo cannot be null");
                }
            }
        }
    }
}
