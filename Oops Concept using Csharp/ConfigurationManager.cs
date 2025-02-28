using System;
using System.Collections.Generic;

public sealed class ConfigurationManager
{
    private static ConfigurationManager _instance;
    private static readonly object _lock = new object();  // Lock for thread safety
    private Dictionary<string, string> settings;

    // Private constructor to prevent direct instantiation
    private ConfigurationManager()
    {
        settings = new Dictionary<string, string>();
    }

    // Public method to get the singleton instance (Thread-Safe)
    public static ConfigurationManager Instance
    {
        get
        {
            if (_instance == null) // First check (without locking)
            {
                lock (_lock)  // Thread-safe locking
                {
                    if (_instance == null) // Second check (ensures only one instance is created)
                    {
                        _instance = new ConfigurationManager();
                    }
                }
            }
            return _instance;
        }
    }

    // Method to set a configuration value
    public void SetConfig(string key, string value)
    {
        settings[key] = value;
    }

    // Method to get a configuration value
    public string GetConfig(string key)
    {
        return settings.ContainsKey(key) ? settings[key] : "Key not found";
    }
    //class Program
    //{
    //    static void Main()
    //    {
    //        // Fetch Singleton instance
    //        ConfigurationManager config1 = ConfigurationManager.Instance;
    //        config1.SetConfig("AppMode", "Dark");
    //        config1.SetConfig("MaxUsers", "100");

    //        // Fetch the instance again
    //        ConfigurationManager config2 = ConfigurationManager.Instance;

    //        // Validate Singleton Behavior
    //        Console.WriteLine("AppMode: " + config2.GetConfig("AppMode")); // Output: Dark
    //        Console.WriteLine("MaxUsers: " + config2.GetConfig("MaxUsers")); // Output: 100

    //        // Checking if both instances are same
    //        Console.WriteLine($"config1 and config2 are same instance: {config1 == config2}"); // Output: True
    //    }
    //}

}
   