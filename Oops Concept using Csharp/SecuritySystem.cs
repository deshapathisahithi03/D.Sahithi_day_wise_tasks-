// Renaming the class to avoid conflict with the existing BankAccount class
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Oops_Concept
{
    public class BankAccountV2
    {
        public string AccountHolder { get; set; }
        public double Balance { get; set; }
        private static double InterestRate; // Static field shared across all instances

        // Constructor
        public BankAccountV2(string accountHolder, double balance)
        {
            AccountHolder = accountHolder;
            Balance = balance;
        }

        // Static method to set interest rate
        public static void SetInterestRate(double rate)
        {
            InterestRate = rate;
            Console.WriteLine($"\nInterest Rate set to {InterestRate}%");
        }

        // Display account details
        public void DisplayDetails()
        {
            Console.WriteLine($"Account Holder: {AccountHolder}, Balance: ${Balance}, Interest Rate: {InterestRate}%");
        }
    }
}
