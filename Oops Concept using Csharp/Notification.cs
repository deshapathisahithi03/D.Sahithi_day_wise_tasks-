using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Oops_Concept
{
    public interface INotificationObserver
    {
        void Update(string message);
    }

    // Concrete Observer: Email Notifier
    public class EmailNotifier : INotificationObserver
    {
        public void Update(string message)
        {
            Console.WriteLine($"Email Notification: {message}");
        }
    }

    // Concrete Observer: SMS Notifier
    public class SMSNotifier : INotificationObserver
    {
        public void Update(string message)
        {
            Console.WriteLine($" SMS Notification: {message}");
        }
    }

    // Subject (Observable) - Notification Service
    public class NotificationService
    {
        private List<INotificationObserver> observers = new List<INotificationObserver>();

        // Subscribe an observer
        public void Subscribe(INotificationObserver observer)
        {
            observers.Add(observer);
        }

        // Unsubscribe an observer
        public void Unsubscribe(INotificationObserver observer)
        {
            observers.Remove(observer);
        }

        // Notify all observers
        public void Notify(string message)
        {
            Console.WriteLine("\n Sending Notifications...");
            foreach (var observer in observers)
            {
                observer.Update(message);
            }
        }

    }
    //class Program
    //{
    //    static void Main()
    //    {
    //        NotificationService notificationService = new NotificationService();

    //        // Create observers
    //        EmailNotifier emailNotifier = new EmailNotifier();
    //        SMSNotifier smsNotifier = new SMSNotifier();

    //        // Subscribe observers
    //        notificationService.Subscribe(emailNotifier);
    //        notificationService.Subscribe(smsNotifier);

    //        // Send notification
    //        notificationService.Notify("New product launch this Friday!");

    //        // Unsubscribe SMS notifier and send another notification
    //        notificationService.Unsubscribe(smsNotifier);
    //        notificationService.Notify("Exclusive discounts for premium members!");
    //    }
    //}
}
