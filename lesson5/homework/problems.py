# Problem 1
# Create a class called BankAccount.
# __init__ takes owner and balance.
# Make a method deposit(amount) that adds to balance.
# Make a method withdraw(amount) that subtracts only if there is enough money.
# Test it with a few deposits and withdrawals.
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Deposited $", amount, ". New balance: $", self.balance)
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrew $", amount, ". New balance: $", self.balance)
        else:
            print("Withdrawal denied: Insufficient funds")
bob = BankAccount("bob", 1000000)
bob.deposit(3285)
bob.withdraw(14453)
bob.deposit(36472)
bob.withdraw(1999999)
# Problem 2
# Create a class called Car.
# __init__ takes model and miles. 
# Make a method drive(distance) that adds to miles.
# Create a Car and drive it a few times, printing miles each time. 
class Car:
    def __init__(self, model, miles):
        self.model = model
        self.miles = miles
    def drive(self, distance):
        self.miles += distance
        print("Miles driven in total:", self.miles)
stingray = Car("Chevrolet Corvette Stingray", 0)
stingray.drive(10)
stingray.drive(74)
stingray.drive(39)
stingray.drive(27)

# Problem 3
# Create a class called ScoreKeeper.
# It stores a dictionary of player scores.
# Make a method add_points(name, points) that adds points for that player.
# Print the final dictionary after adding points for a few players.
class ScoreKeeper:
    def __init__(self,):
        self.scores = {}
    def add_points(self, name, points):
        if name in self.scores:
            self.scores[name] += points
        else:
            self.scores[name] = points
scores = ScoreKeeper()
scores.add_points
scores.add_points("Alice", 10)
scores.add_points("Bob", 5)
scores.add_points("Alice", 3)  
scores.add_points("Charlie", 7)
scores.add_points("Bob", 10)
print("Final scores:", scores.scores)
# Problem 4
# Create a class called Timer.
# It starts at 0 seconds.
# Make a method tick() that adds 1.
# Make a method reset() that sets it back to 0.
# Test tick() and reset().
class Timer:
    def __init__(self, time):
        self.time = time
    def tick(self):
        self.time += 1
        print("Time:", self.time)
    def reset(self):
        self.time = 0
        print("Time reset to 0")
my_timer = Timer(0)
my_timer.tick()
my_timer.tick()
my_timer.tick()
my_timer.tick()
my_timer.reset()
my_timer.tick()
my_timer.reset()
# Problem 5
# Create a class called WordTracker.
# It stores a word (string).
# Make a method add_letter(letter) that adds the letter to the end.
# Make a method remove_last() that removes the last letter (if it exists).
# Test it.
class WordTracker:
    def __init__(self):
        self.word = "walk"
        print(self.word)
    def add_letter(self, letter):
        self.word = self.word + letter
        print(self.word)
    def remove_last(self):
        self.word = self.word[:-1]
        print(self.word)
word = WordTracker()
word.add_letter("i")
word.add_letter("n")
word.add_letter("g")
word.remove_last()
word.remove_last()
word.remove_last()