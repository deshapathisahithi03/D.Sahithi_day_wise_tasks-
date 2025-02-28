using System;

// Strategy Interface
public interface IDiscountStrategy
{
    decimal ApplyDiscount(decimal totalAmount);
}

// Concrete Strategy: No Discount
public class NoDiscount : IDiscountStrategy
{
    public decimal ApplyDiscount(decimal totalAmount)
    {
        return totalAmount; // No discount applied
    }
}

// Concrete Strategy: Percentage-Based Discount
public class PercentageDiscount : IDiscountStrategy
{
    private readonly decimal _percentage;

    public PercentageDiscount(decimal percentage)
    {
        _percentage = percentage;
    }

    public decimal ApplyDiscount(decimal totalAmount)
    {
        return totalAmount - (totalAmount * _percentage / 100);
    }
}

// Concrete Strategy: Fixed Amount Discount
public class FixedAmountDiscount : IDiscountStrategy
{
    private readonly decimal _fixedAmount;

    public FixedAmountDiscount(decimal fixedAmount)
    {
        _fixedAmount = fixedAmount;
    }

    public decimal ApplyDiscount(decimal totalAmount)
    {
        return Math.Max(totalAmount - _fixedAmount, 0); // Ensures total is not negative
    }
}

// Context: Shopping Cart
public class ShoppingCart
{
    private IDiscountStrategy _discountStrategy;
    public decimal TotalAmount { get; set; }

    // Constructor
    public ShoppingCart(decimal totalAmount)
    {
        TotalAmount = totalAmount;
        _discountStrategy = new NoDiscount(); // Default strategy
    }

    // Set the discount strategy dynamically
    public void SetDiscountStrategy(IDiscountStrategy discountStrategy)
    {
        _discountStrategy = discountStrategy;
    }

    // Calculate final amount after applying discount
    public decimal GetFinalAmount()
    {
        return _discountStrategy.ApplyDiscount(TotalAmount);
    }
}

// Main Program
class Program
{
    static void Main()
    {
        Console.Write("Enter total amount: ");
        decimal totalAmount = Convert.ToDecimal(Console.ReadLine());

        ShoppingCart cart = new ShoppingCart(totalAmount);

        Console.Write("Choose Discount Type (None/Percentage/Fixed): ");
        string discountType = Console.ReadLine().ToLower();

        switch (discountType)
        {
            case "percentage":
                Console.Write("Enter discount percentage: ");
                decimal percent = Convert.ToDecimal(Console.ReadLine());
                cart.SetDiscountStrategy(new PercentageDiscount(percent));
                break;

            case "fixed":
                Console.Write("Enter fixed discount amount: ");
                decimal fixedAmount = Convert.ToDecimal(Console.ReadLine());
                cart.SetDiscountStrategy(new FixedAmountDiscount(fixedAmount));
                break;

            default:
                cart.SetDiscountStrategy(new NoDiscount());
                break;
        }

        Console.WriteLine($"\nFinal amount after discount: {cart.GetFinalAmount():C}");
    }
}
