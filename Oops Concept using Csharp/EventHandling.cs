using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Oops_Concept
{
    public delegate void ButtonClickHandler(string buttonName);

    // Button class with event
    class Button
    {
        public string Name { get; set; }

        // Event declaration
        public event ButtonClickHandler OnClick;

        public Button(string name)
        {
            Name = name;
        }

        // Method to simulate a button click
        public void Click()
        {
            Console.WriteLine($"\n{Name} button clicked.");
            OnClick?.Invoke(Name); // Trigger event if there are subscribers
        }
    }

    // Class that listens to button events
    class UserInterface
    {
        // Method to respond to button clicks
        public void ButtonClickedResponse(string buttonName)
        {
            Console.WriteLine($"Action triggered for {buttonName} button.");
        }
    }
}
