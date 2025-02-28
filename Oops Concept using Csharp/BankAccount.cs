using System;

namespace Oops_Concept
{
    public class BankAccount
    {
        private float balance;

        public BankAccount(double initialBalance)
        {
            if (initialBalance < 0)
            {
                throw new ArgumentOutOfRangeException("Initial balance must be greater than zero");
            }
            else if (initialBalance > 10000)
            {
                throw new ArgumentOutOfRangeException("Initial balance must be less than 10000");
            }
            else
            {
                balance = (float)initialBalance;
            }
        }

        public void Deposit(double amount)
        {
            if (amount < 0)
            {
                throw new ArgumentOutOfRangeException("Deposit amount must be greater than zero");
            }
            else if (amount > 10000)
            {
                throw new ArgumentOutOfRangeException("Deposit amount must be less than 10000");
            }
            else
            {
                balance += (float)amount;
                Console.WriteLine($"Deposited: {amount:C}. New Balance: {balance:C}");
            }
        }

        public void Withdraw(double amount)
        {
            if (amount < 0)
            {
                throw new ArgumentOutOfRangeException("Withdraw amount must be greater than zero");
            }
            else if (amount > 10000)
            {
                throw new ArgumentOutOfRangeException("Withdraw amount must be less than 10000");
            }
            else if (amount > balance)
            {
                Console.WriteLine("Insufficient balance.");
            }
            else
            {
                balance -= (float)amount;
                Console.WriteLine($"Withdrew: {amount:C}. New Balance: {balance:C}");
            }
        }

        public float GetBalance()
        {
            return balance;
        }
    }


}
