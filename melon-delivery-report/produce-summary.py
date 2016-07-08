
def deliveryReport(fileName):

    the_file = open(fileName)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print "Delivered {} {}s for total of ${}".format(count, melon, amount)
    the_file.close()


deliveryReport("um-deliveries-20140519.txt")

deliveryReport("um-deliveries-20140520.txt")

deliveryReport("um-deliveries-20140521.txt")


