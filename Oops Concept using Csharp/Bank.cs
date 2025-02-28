using System;

// Bank class
class Bank
{
    public string AccountHolder { get; set; }
    public double Balance { get; set; }
    private static double InterestRate; // Static field

    // Constructor
    public Bank(string accountHolder, double balance)
    {
        AccountHolder = accountHolder;
        Balance = balance;
    }

    // Static method to set interest rate
    public static void SetInterestRate(double rate)
    {
        InterestRate = rate;
        Console.WriteLine($"Interest Rate set to {InterestRate}%");
    }

    // Display account details
    public void DisplayDetails()
    {
        Console.WriteLine($"Account Holder: {AccountHolder}, Balance: ${Balance}, Interest Rate: {InterestRate}%");
    }
}
