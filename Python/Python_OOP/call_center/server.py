class Call(): 
    def __init__(self, ID, caller_name, number, time, reason):
        self.ID = ID
        self.caller_name = caller_name
        self.number = number
        self.time = time
        self.reason = reason
    def display(self):
        print "ID: " + self.ID
        print "Name: " + self.caller_name
        print "Phone Number: " + self.number
        print "Time: " + self.time
        print "Reason: " + self.reason

class CallCenter():
    def __init__(self):
        self.calls = []
        self.queueSize = len(self.calls)

    def add(self, call):
        if isinstance(call, list):
            for num in range(0, len(call)):
                self.calls.append(call[num])
        else:
            self.calls.append(call)

        self.queueSize = len(self.calls)
        return self

        def remove(self):
        del calls[0]
        return self

    def remove(self, pNum):
        for call in self.calls:
            if call.phNumber == pNum:
                self.calls.remove(call)

    def info(self):
        for call in self.calls:
            print "{} ({}) --Queue Length: {}".format(call.name, call.phNumber, self.queueSize)
        print ""

c1 = Call("01", "Dan", "630303030303", "9AM", "reason")
c2 = Call("02", "Pete", "12335", "10AM", "reason2")
c1.display()


Cc1 = CallCenter()
Cc1.add(c1)
Cc1.add(c2)

print c1
print c2

print Cc1.calls





