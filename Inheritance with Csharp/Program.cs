using System.Net;
using System.Net.Sockets;

namespace Inheritance_with_Csharp
{
    internal class Program
    {
        static void Main(string[] args)
        {
           // Console.WriteLine("1*******************************************");
           // Console.WriteLine("Enter the brand of the car and Bike ");
           // string brand1 = Console.ReadLine();
           // string brand2 = Console.ReadLine();
           // Console.WriteLine("Enter the speed of the car and Bike  ");
           // int speed1 = Convert.ToInt32(Console.ReadLine());
           // int speed2 = Convert.ToInt32(Console.ReadLine());

           // Car car = new();
           // car.Brand = brand1;
           // car.Speed = speed1;

           // car.DisplayInfo();

           // Bike bike = new();
           // bike.Brand = brand2;
           // bike.Speed = speed2;
           // bike.DisplayInfo();
           // Console.WriteLine("2*******************************************");
           // Console.WriteLine("Enter the home address of the car and bike");
           // string address1 = Console.ReadLine();
           // string address2 = Console.ReadLine();

           // Console.WriteLine("Using the Vehicle2 class");
           // Car2 car2 = new Car2(brand1, speed1);
           // car2.DisplayInfo();
           // car2.Homeadress(address1); // Corrected method name
           // Bike2 bike2 = new Bike2(brand2, speed2);
           // bike2.DisplayInfo();
            
           // bike2.Homeaddress(address2); // Corrected method name

           // Console.WriteLine("3*******************************************");
           // Console.WriteLine("Enter the details of Manager");
           // Console.WriteLine("Enter the name of the Manager");
           // string name = Console.ReadLine();
           // Console.WriteLine("Enter the salary of the Manager");
           // int salary = Convert.ToInt32(Console.ReadLine());
           // Console.WriteLine("enter the bonus of the Manager");
           // int bonus = Convert.ToInt32(Console.ReadLine());

           // Manager manager = new(name, salary, bonus);
           // manager.DisplayInfo();
           // manager.DisplayInfo2();
           // Console.WriteLine("4*******************************************");
           // Animal cat=new Dog();
           // cat.MakeSound();
           //Animal dog = new Cat();
           // dog.MakeSound();
            //Console.WriteLine("5*******************************************");
            //Robot robot = new Robot();
            //robot.start();
            //robot.Move();

            //Console.WriteLine("6*******************************************");

            //SavingsAccount savingsAccount = new SavingsAccount();
            //savingsAccount.CalculateInterest();

            //Console.WriteLine("7*******************************************");
            //Duck duck = new Duck();
            //duck.Fly();
            //duck.Swim();

            //Console.WriteLine("8*******************************************");
            //Person person = new Student();
            //person.Greet();
            //if (person is Student)
            //{
            //    Student student = (Student)person;
            //    student.Study();
            //}

            //Console.WriteLine("9*******************************************");

            //Console.WriteLine("Enter the details of Product");
            //Console.WriteLine("Enter product type (Electronic/Clothing):");
            //string productType = Console.ReadLine()?.Trim().ToLower();

            //Console.Write("Enter product name: ");
            //string name = Console.ReadLine();

            //Console.Write("Enter product price: ");
            //double price;
            //while (!double.TryParse(Console.ReadLine(), out price) || price <= 0)
            //{
            //    Console.Write("Invalid price. Enter a valid positive number: ");
            //}

            //Product product;

            //if (productType == "electronic")
            //{
            //    product = new ElectronicProduct(name, price);
            //}
            //else if (productType == "clothing")
            //{
            //    product = new ClothingProduct(name, price);
            //}
            //else
            //{
            //    Console.WriteLine("Invalid product type. Defaulting to a regular product.");
            //    product = new Product(name, price);
            //}

            //product.DisplayInfo();

            Console.WriteLine("10*******************************************");
            Bank bank = new Bank();
            bank.DoBanking();


        }
    }
}
    