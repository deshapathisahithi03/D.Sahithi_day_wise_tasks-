using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Oops_Concept
{
        public interface ILogger
        {
            void Log(string message);
        }

        // Concrete FileLogger class
        public class FileLogger : ILogger
        {
            public void Log(string message)
            {
                Console.WriteLine($"[File Log]: {message}");
            }
        }

        // Base Decorator class (inherits from ILogger)
        public abstract class LoggerDecorator : ILogger
        {
            protected ILogger _logger;

            public LoggerDecorator(ILogger logger)
            {
                _logger = logger;
            }

            public virtual void Log(string message)
            {
                _logger.Log(message);
            }
        }

        // Concrete Decorator: Adds Timestamp
        public class TimestampLogger : LoggerDecorator
        {
            public TimestampLogger(ILogger logger) : base(logger) { }

            public override void Log(string message)
            {
                string timestamp = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");
                base.Log($"[{timestamp}] {message}");
            }
        }

        // Concrete Decorator: Adds Error Categorization
        public class ErrorLogger : LoggerDecorator
        {
            public ErrorLogger(ILogger logger) : base(logger) { }

            public override void Log(string message)
            {
                base.Log($"[ERROR] {message}");
            }
        }
}
