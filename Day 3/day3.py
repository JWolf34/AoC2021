import os

with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"3.txt"))) as f:
    input = f.read().splitlines()

def part1():
    gamma = ''
    epsilon = ''

    for i in range(0, len(input[0])):
        zeros = 0
        ones = 0
        for bit in input:
            if bit[i] == '0':
                zeros += 1
            elif bit[i] == '1':
                ones += 1

        if (zeros > ones):
            gamma += '0'
            epsilon += '1'
        elif(ones > zeros):
            gamma += '1'
            epsilon += '0'
        else:
            print("They're equal?")
        
    print("Gamma: {}".format(gamma))
    print("Epsilon: {}".format(epsilon))

    gamma_dec = int(gamma, 2)
    epsilon_dec = int(epsilon, 2)
    print ("Mulitply in decimal: {}".format(str(gamma_dec * epsilon_dec)))




def part2():

    bits = input[:]
    to_be_deleted ={'ones': [], 'zeros': []}

    for i in range(0, len(bits[0])):
        if len(bits) == 1:
            break
        zeros = 0
        ones = 0
        for j in range(0, len(bits)):
            if bits[j][i] == '0':
                zeros += 1
                to_be_deleted["zeros"].append(j)
            elif bits[j][i] == '1':
                ones += 1
                to_be_deleted["ones"].append(j)
        if (zeros > ones):
            for index in to_be_deleted["ones"]:
                bits[index] = 'to_be_deleted'
        elif(ones > zeros or ones == zeros):
            for index in to_be_deleted["zeros"]:
                bits[index] = "to_be_deleted"
    
        bits = list(filter(lambda x: x != 'to_be_deleted', bits))  
        to_be_deleted['ones'].clear()
        to_be_deleted['zeros'].clear()
        #print(bits)
        #print('---------------------------------------')
    oxy = bits[0]

    bits = input[:]

    for i in range(0, len(bits[0])):
        if len(bits) == 1:
            break
        zeros = 0
        ones = 0
        for j in range(0, len(bits)):
            bit = bits[j][i]
            if bits[j][i] == '0':
                zeros += 1
                to_be_deleted["zeros"].append(j)
            elif bits[j][i] == '1':
                ones += 1
                to_be_deleted["ones"].append(j)
        if (zeros > ones):
            for index in to_be_deleted["zeros"]:
                bits[index] = 'to_be_deleted'
        elif(ones > zeros or ones == zeros):
            for index in to_be_deleted["ones"]:
                bits[index] = "to_be_deleted"
    
        bits = list(filter(lambda x: x != 'to_be_deleted', bits))  
        to_be_deleted['ones'].clear()
        to_be_deleted['zeros'].clear()
        #print(bits)
        #print('---------------------------------------')  
    co2 = bits[0]  

    print("Oxygen: {}".format(oxy))
    print("CO2: {}".format(co2))
    print ("Mulitply in decimal: {}".format(str(int(oxy, 2) * int(co2,2))))

if __name__ == '__main__':
    #part1()
    part2()