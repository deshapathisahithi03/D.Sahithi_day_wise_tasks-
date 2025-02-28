using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Oops_Concept
{
    interface IPrintable
    {
        void Print();
    }

    // Defining the ISerializable interface
    interface ISerializable
    {
        void Serialize();
    }

    // Implementing both interfaces in the Report class
    class Report : IPrintable, ISerializable
    {
        public string Title { get; set; }
        public string Content { get; set; }

        public void Print()
        {
            Console.WriteLine($"Printing Report: {Title}\n{Content}");
        }
    

        public void Serialize()
        {
    string filePath = "report.txt";
            File.WriteAllText(filePath, $"Title: {Title}\nContent: {Content}");
            Console.WriteLine($"Report serialized to {filePath}");
        }
    }
   
}
