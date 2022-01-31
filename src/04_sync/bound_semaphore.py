import random
import threading
import time


class TicketSeller(threading.Thread):
    ticketsSold = 0

    def __init__(self, semaphore):
        threading.Thread.__init__(self)
        self.sem = semaphore
        print("Ticket Seller Started Work")

    def run(self):
        global ticketsAvailable
        running = True
        while running:
            delay = self.randomDelay()

            self.sem.acquire()
            if(ticketsAvailable <= 0):
                running = False
            else:
                self.ticketsSold = self.ticketsSold + 1
                ticketsAvailable = ticketsAvailable - 1
                print(f'{self.name} Sold One ({ticketsAvailable} left) - {delay}s')
            self.sem.release()
        print(
            f'Ticket Seller {self.name} Sold {self.ticketsSold} tickets in total')

    def randomDelay(self):
        delay = random.randint(0, 4)/4
        time.sleep(delay)
        return delay


# our sempahore primitive
semaphore = threading.BoundedSemaphore(4)
# Our Ticket Allocation
ticketsAvailable = 200

# our array of sellers
sellers = []
for i in range(4):
    seller = TicketSeller(semaphore)
    seller.start()
    sellers.append(seller)

# joining all our sellers
for seller in sellers:
    seller.join()
