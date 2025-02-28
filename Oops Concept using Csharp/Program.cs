//using Oops_Concept;
//using System;

//namespace Oops_Concept
//{
//    public class Program
//    {
//         static void Main(string[] args) { 

//Console.Write("Enter initial balance: ");
//decimal initialBalance = Convert.ToDecimal(Console.ReadLine());

//BankAccount account = new((double)initialBalance);

//Console.Write("Enter deposit amount: ");
//decimal depositAmount = Convert.ToDecimal(Console.ReadLine());
//account.Deposit((double)depositAmount);

//Console.Write("Enter withdrawal amount: ");
//decimal withdrawAmount = Convert.ToDecimal(Console.ReadLine());
//account.Withdraw((double)withdrawAmount);

//Console.WriteLine($"Final Balance: {account.GetBalance():C}");

//Console.WriteLine("enter name");
//string? name = Console.ReadLine();

//Console.WriteLine("enter rollno");
//string? rollno = Console.ReadLine();

//Students_Details students_Details = new Students_Details();
//students_Details.Name = name;
//students_Details.RollNo = rollno;
//Console.WriteLine($"Name: {students_Details.Name}");
//Console.WriteLine($"RollNo: {students_Details.RollNo}");

//Console.WriteLine("Choose book entry method:\n1. Default Book\n2. Title & Author\n3. Title, Author & ISBN");
//Console.Write("Enter your choice: ");
//string choice = Console.ReadLine();

//Book book;

//switch (choice)
//{
//    case "1":
//        book = new Book();
//        break;

//    case "2":
//        Console.Write("Enter book title: ");
//        string title1 = Console.ReadLine();

//        Console.Write("Enter author name: ");
//        string author1 = Console.ReadLine();

//        book = new Book(title1, author1);
//        break;

//    case "3":
//        Console.Write("Enter book title: ");
//        string title2 = Console.ReadLine();

//        Console.Write("Enter author name: ");
//        string author2 = Console.ReadLine();

//        Console.Write("Enter ISBN: ");
//        string isbn = Console.ReadLine();

//        book = new Book(title2, author2, isbn);
//        break;

//    default:
//        Console.WriteLine("Invalid choice! Creating a default book.");
//        book = new Book();
//        break;
//}

////book.Display();
//Console.WriteLine("enter radius");
//double radius = Convert.ToDouble(Console.ReadLine());
//Circle circle = new Circle(radius);
//Console.WriteLine($"Area of circle: {circle.CalculateArea()}");
//Console.WriteLine("enter length");
//double length = Convert.ToDouble(Console.ReadLine());
//Console.WriteLine("enter breadth");
//double breadth = Convert.ToDouble(Console.ReadLine());
//Rectangle rectangle = new Rectangle(length, breadth);
//Console.WriteLine($"Area of rectangle: {rectangle.CalculateArea()}");

//Car car = new Car();
//car.start();
//Bike bike = new Bike();
//bike.start();



//Console.WriteLine("Enter type (Student/Teacher): ");
//string type = Console.ReadLine().Trim().ToLower();

//Person person;

//Console.Write("Enter Name: ");
//string names = Console.ReadLine();

//Console.Write("Enter Age: ");
//int age = int.Parse(Console.ReadLine());

//if (type == "student")
//{
//    Console.Write("Enter Student ID: ");
//    string studentID = Console.ReadLine();
//    person = new Student { Name = name, Age = age, StudentID = studentID };
//}
//else if (type == "teacher")
//{
//    Console.Write("Enter Subject: ");
//    string subject = Console.ReadLine();
//    person = new Teacher { Name = name, Age = age, Subject = subject };
//}
//else
//{
//    Console.WriteLine("Invalid type! Exiting...");
//    return;
//}

//Console.WriteLine("\nDetails:");
//person.GetDetails();

//            //Calculator calculator = new Calculator();
//            //Console.WriteLine("Enter first number");
//            //int num1 = Convert.ToInt32(Console.ReadLine());
//            //Console.WriteLine("Enter second number");
//            //int num2 = Convert.ToInt32(Console.ReadLine());
//            //int result = num1 + num2;
//            //Console.WriteLine("Addition of two numbers is: " + calculator.Add(num1, num2));

//            Calculator calc = new Calculator();

//            // Demonstrating method overloading
//            Console.WriteLine("Addition of two integers: " + calc.Add(5, 10));
//            Console.WriteLine("Addition of three integers: " + calc.Add(3, 6, 9));
//            Console.WriteLine("Addition of two doubles: " + calc.Add(2.5, 4.7));

//            MusicPlayer musicPlayer = new MusicPlayer();
//            musicPlayer.play();
//            VideoPlayer videoPlayer = new VideoPlayer();
//            videoPlayer.play();

//            Report report = new Report { Title = "Monthly Sales", Content = "Sales increased by 20% this month." };

//            report.Print();        // Calls Print() from IPrintable
//            report.Serialize();

//            User admin = new Admin {
//                Username = "AdminUser"
//            };
//            User customer = new Customer { 
//                Username = "CustomerUser" 
//            };

//            Console.WriteLine($"{admin.Username}'s Access:");
//            admin.AccessControl(); // Calls Admin's AccessControl()

//            Console.WriteLine($"\n{customer.Username}'s Access:");
//            customer.AccessControl(); // Calls Customer's AccessControl()

//            Console.WriteLine("Enter the real part of the first complex number:");
//            double real1 = double.Parse(Console.ReadLine());

//            Console.WriteLine("Enter the imaginary part of the first complex number:");
//            double imag1 = double.Parse(Console.ReadLine());

//            // Taking user input for second complex number
//            Console.WriteLine("Enter the real part of the second complex number:");
//            double real2 = double.Parse(Console.ReadLine());

//            Console.WriteLine("Enter the imaginary part of the second complex number:");
//            double imag2 = double.Parse(Console.ReadLine());

//            // Creating complex number objects
//            ComplexNumber c1 = new ComplexNumber(real1, imag1);
//            ComplexNumber c2 = new ComplexNumber(real2, imag2);

//            // Adding the two complex numbers
//            ComplexNumber sum = c1 + c2;

//            // Displaying the result
//            Console.WriteLine($"\nResult of Addition: {sum}");


//            // Taking user input for Department and Manager
//            Console.Write("Enter Department Name: ");
//            string deptName = Console.ReadLine();

//            Console.Write("Enter Manager Name: ");
//            string managerName = Console.ReadLine();

//            // Creating original Department object
//            Department original = new Department(deptName, new Manager(managerName));

//            // Creating copies
//            Department shallowCopy = original.ShallowCopy();
//            Department deepCopy = original.DeepCopy();

//            // Display initial values
//            Console.WriteLine("\nBefore modifying copies:");
//            Console.WriteLine($"Original Manager: {original.Manager.Name}");
//            Console.WriteLine($"Shallow Copy Manager: {shallowCopy.Manager.Name}");
//            Console.WriteLine($"Deep Copy Manager: {deepCopy.Manager.Name}");

//            // Asking user to modify the Manager's name in the shallow copy
//            Console.Write("\nEnter new Manager Name for the Shallow Copy: ");
//            shallowCopy.Manager.Name = Console.ReadLine();

//            // Display values after modification
//            Console.WriteLine("\nAfter modifying the shallow copy's Manager:");
//            Console.WriteLine($"Original Manager: {original.Manager.Name}");  // Affected
//            Console.WriteLine($"Shallow Copy Manager: {shallowCopy.Manager.Name}");  // Modified value
//            Console.WriteLine($"Deep Copy Manager: {deepCopy.Manager.Name}");  // Unaffected


//            // Setting the interest rate
//            Bank.SetInterestRate(5.0);

//            // Creating two bank accounts
//            Bank account1 = new Bank("Alice", 1000);
//            Bank account2 = new Bank("Bob", 2000);

//            // Displaying account details before changing interest rate
//            Console.WriteLine("\nBefore changing the interest rate:");
//            account1.DisplayDetails();
//            account2.DisplayDetails();

//            // Changing interest rate
//            Bank.SetInterestRate(6.5);

//            // Displaying account details after changing interest rate
//            Console.WriteLine("\nAfter changing the interest rate:");
//            account1.DisplayDetails();
//            account2.DisplayDetails();

//            Console.Write("Enter initial interest rate: ");
//            double initialRate = double.Parse(Console.ReadLine());
//            Bank.SetInterestRate(initialRate);

//            // Taking user input for bank accounts
//            Console.Write("\nEnter the number of accounts: ");
//            int numAccounts = int.Parse(Console.ReadLine());

//            Bank[] accounts = new Bank[numAccounts];

//            for (int i = 0; i < numAccounts; i++)
//            {
//                Console.Write($"\nEnter account holder name for Account {i + 1}: ");
//                string namess = Console.ReadLine();

//                Console.Write($"Enter initial balance for {name}: ");
//                double balance = double.Parse(Console.ReadLine());

//                accounts[i] = new Bank(name, balance);
//            }

//            // Displaying account details before changing interest rate
//            Console.WriteLine("\nBefore updating interest rate:");
//            foreach (var acc in accounts)
//            {
//                acc.DisplayDetails();
//            }

//            // Changing interest rate
//            Console.Write("\nEnter new interest rate: ");
//            double newRate = double.Parse(Console.ReadLine());
//            Bank.SetInterestRate(newRate);

//            // Displaying account details after changing interest rate
//            Console.WriteLine("\nAfter updating interest rate:");
//            foreach (var acc in accounts)
//            {
//                acc.DisplayDetails();
//            }

//            Button myButton = new Button("Submit");

//            // Create a UserInterface instance and subscribe to the button event
//            UserInterface ui = new UserInterface();
//            myButton.OnClick += ui.ButtonClickedResponse;

//            // Simulate button clicks
//            myButton.Click();
//            myButton.Click();

//            Console.Write("Enter vehicle type (Car/Bike): ");
//            string vehicleType = Console.ReadLine();

//            try
//            {
//                IVehicle vehicle = VehicleFactory.GetVehicle(vehicleType);
//                vehicle.Drive();  // Calls the respective Drive() method
//            }
//            catch (Exception ex)
//            {
//                Console.WriteLine($"Error: {ex.Message}");
//            }

//            public interface ILogger
//        {
//            void Log(string message);
//        }

//        // Concrete FileLogger class
//        public class FileLogger : ILogger
//        {
//            public void Log(string message)
//            {
//                Console.WriteLine($"[File Log]: {message}");
//            }
//        }

//        // Base Decorator class (inherits from ILogger)
//        public abstract class LoggerDecorator : ILogger
//        {
//            protected ILogger _logger;

//            public LoggerDecorator(ILogger logger)
//            {
//                _logger = logger;
//            }

//            public virtual void Log(string message)
//            {
//                _logger.Log(message);
//            }
//        }

//        // Concrete Decorator: Adds Timestamp
//        public class TimestampLogger : LoggerDecorator
//        {
//            public TimestampLogger(ILogger logger) : base(logger) { }

//            public override void Log(string message)
//            {
//                string timestamp = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");
//                base.Log($"[{timestamp}] {message}");
//            }
//        }

//        // Concrete Decorator: Adds Error Categorization
//        public class ErrorLogger : LoggerDecorator
//        {
//            public ErrorLogger(ILogger logger) : base(logger) { }

//            public override void Log(string message)
//            {
//                base.Log($"[ERROR] {message}");
//            }

          
//        }
//    }


//}
