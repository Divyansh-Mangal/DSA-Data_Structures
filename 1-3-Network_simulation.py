#python3

#Defining queue class
class Queue():
    def __init__(self,size):
        self.size = size
        self.Q = [None]*self.size
        self.head = 0
        self.tail = 0

    def add2Q(self,num):
        self.Q[self.head] = num
        if self.head != self.size-1:
            self.head += 1
        else:
            self.head = 0


    def remove(self):
        self.Q[self.tail] = None
        if self.tail != self.size-1:
            self.tail += 1
        else:
            self.tail = 0


def network_simulation(s, n, packets):
    # Packets list empty?
    if len(packets) == 0:
        return []

    #setup intial conditions
    buffer = Queue(s)
    time = 0
    index = 0
    removal_time = packets[0][0] + packets[0][1]
    begin_time = [None]*len(packets)

    complete = False
    while not complete:

        #removing processed package
        if buffer.Q[buffer.tail] != None and removal_time == time:

            begin_time[buffer.Q[buffer.tail]] = time - packets[buffer.Q[buffer.tail]][1]
            buffer.remove()

            if buffer.Q[buffer.tail] != None:
                removal_time = time + packets[buffer.Q[buffer.tail]][1]


        #add next package
        if index >= len(packets):
            pass
        elif packets[index][0] == time:

            if packets[index][1] == 0:
                begin_time[index] = packets[index][0]
                removal_time = time
                index += 1 

            elif buffer.Q[buffer.head] == None :
                buffer.add2Q(index)
                index += 1

            elif buffer.Q[buffer.head] != None :
                begin_time[index] = -1
                index += 1

        if index >= len(packets):
            time += 1
        else:
            if time == packets[index][0]:
                pass
            else:
                time += 1

        if index >= len(packets):
            for cell in buffer.Q:
                if cell != None:
                    complete = False
                    break
                else:
                    complete = True


    return begin_time

if __name__ == '__main__':
    with open('D:\\Transcendence\\Route_Computing\\Coursera - Data Structure and Algorithms - UCSD\\course_2_Data_Structures\\week1_basic_data_structures\\3_network_simulation\\tests\\03') as f:

        #numstring = list(map(int, input().split()))
        numstring = list(map(int, f.read().split()))
        s = numstring[0]
        n = numstring[1]
        packets = list(zip(numstring[2::2], numstring[3::2]))

        print(network_simulation(s, n, packets))
    ans = network_simulation(s, n, packets)
    for num in ans:
        print(num)
