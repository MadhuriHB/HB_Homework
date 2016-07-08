
#Create a function that takes in a text file of customer orders and parses it to produce similar output

def expected_pay(num_melons):           # Calculates pay for no. of melons
    pay = num_melons * 1.00
    return pay



def customer_paid_cost(customer_file):   # compares paid and expected
    input_file = open(customer_file)
    for line in input_file:
        words = line.split("|")
        name = words[1]
        melons = float(words[2])
        paid = float(words[3])
        expected = expected_pay(melons)
        if expected != paid:
            print name, "paid {:.2f}, expected {:.2f}".format(paid, expected)

    input_file.close()


# customer_paid_cost("Joe", 5.00, 5)
# customer_paid_cost("Frank", 6.00, 6)
# customer_paid_cost("Sean", 9.00, 9)
# customer_paid_cost("David", 4.00, 4)
# customer_paid_cost("Ashley", 2.00, 3)
# customer_paid_cost("Sally", 3.00, 3)

customer_paid_cost("customer-orders.txt")
