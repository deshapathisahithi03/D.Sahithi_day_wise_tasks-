import threading
import time

class TicketBooking:
    def __init__(self, total_tickets):
        self.total_tickets = total_tickets
        self.lock = threading.Lock()

    def available_tickets(self):
        with self.lock:
            return self.total_tickets

    def book_ticket(self, name):
        with self.lock:
            if self.total_tickets > 0:
                print(f"{name} is trying to book... (Available: {self.total_tickets})")
                time.sleep(1)  # Simulate processing time
                if self.total_tickets > 0:  # Double-check to avoid overselling
                    self.total_tickets -= 1
                    print(f" {name} successfully booked a ticket! Remaining: {self.total_tickets}")
                else:
                    print(f" {name}, ticket just sold out!")
            else:
                print(f" {name}, no tickets available.")

# Initialize with 1 ticket
booking_system = TicketBooking(total_tickets=1)

# Simulating 2 users trying to book at the same time
users = ["Alice", "Bob"]
threads = []

for user in users:
    t = threading.Thread(target=booking_system.book_ticket, args=(user,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print(" Booking process completed.")
