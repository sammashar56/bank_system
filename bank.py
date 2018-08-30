# objects and classes
# inheritance
# polymorphism
# abstraction
# overriding, overloading
# constructors


# state and behaviors: real world
# car: states: color, type, model, year, no of wheels, doors
# behaviors:   accelerate, move

# in programming: states becomes  properties/fields
# behaviors becomes functions/methods

import sqlite3
import time
import datetime
class Account:
    conn = sqlite3.connect('bank2.db')
    conn = sqlite3.connect('deposits.db')
    conn = sqlite3.connect('withdraw.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS bank(
               name text,
               branch text,
               amount integer,
               pin integer
               )""")

    c.execute("""CREATE TABLE IF NOT EXISTS deposits(
                 acc_id integer,
                 deposit integer 
                 )""")

    c.execute("""CREATE TABLE IF NOT EXISTS withdrawn(
                     pin integer,
                     wth integer 
                     )""")
    #date = str(datetime.datetime.timestamp(unix).strftime)

    def __init__(self, name, branch, amount, pin):
        self.amt = amount
        self.name = name
        self.branch = branch
        self.pin = pin
        self.save(name, branch, amount, pin)

    def save(self, name, branch, amount, pin):
        self.c.execute('''INSERT INTO bank VALUES(?,?,?,?)''', (name, branch, amount, pin))
        self.conn.commit()
        print("Saved")

    def login(self, pin):
        if self.pin == pin:
            print('logged in')
            return True
        else:
            print('wrong password')
            return False

    def deposit(self, acc_id, dep):
        self.c.execute('''INSERT INTO deposits VALUES(?,?)''', (acc_id, dep))
        self.conn.commit()
        print('saved')
        print('you have deposited', dep)
        #an error in this line.
        self.amt = self.amt + dep
        print('total amount is ', self.amt)

    def check(self, cash):
         if cash < self.amt:
             if self.amt < 100:
                 return 1
             else:
                 return 2
         else:
             return 3

    def check233(self, cash):
        if cash > self.amt and self.amt < 100:
            return 3
        else:
            return 2

    def withdrawal(self, pin, wth):
       # tick = time.time()
        self.c.execute('''INSERT INTO withdrawn VALUES(?,?)''', (pin, wth))
        self.conn.commit()
        print('saved')
        print('you have deposited', wth)
        profits = []
        if self.pin == pin:
            if self.check(wth) == 3:
                print('Insufficient Bal')
            elif self.check(wth) == 1:
                print('to withdraw bal > 100')

            elif self.check(wth) == 2:
                self.amt = self.amt - wth
                print('you have successfully withdrawn', wth, 'balance =', self.amt)
                x = 20
                profits.append(x)
                print(profits)
            else:
                print("Error")
        else:
            print('wrong pin')

    def check_details(self):
            print(self.name, self.amt, self.pin, self.branch)


obj = Account(input("Enter Name"), input("Enter branch "), int(input("Enter Amount")), int(input("Enter PIN")))


#obj.login(565)
#obj.withdrawal()
#obj.deposit(int(input('Enter Acc')), int(input("How much to dep")))
obj.withdrawal(int(input('Enter pin')), int(input("How much to withdraw")))
#obj.check_details()





























