import  cmath, numpy, math
print("\n\n-----------------------------------------------------\n\n")
while(True):
    choice = input("Hello, please create a basis; select an option below\n1. Pre-set Basis \n2. Custom Basis\n")
    if (choice == "1"):
        while(True):
            choice2 = input("Choose one of the following basis (in degrees)\n1. {0,90}\n2. {-45,45}\n3. {30,120}")
            if (choice2 == "1"):
                basis = ("0","90")
                break
            if (choice2 == "2"):
                basis = ("-45","45")
                break
            if (choice2 == "3"):
                basis = ("30","120")
                break
        break
    if (choice == "2"):
        while(True):
            in1 = input("What is the first degree in the basis?\n")
            in2 = input("What is the second degree in the basis?\n")
            if(int(in1)+90 == int(in2) or int(in2)+90 == int(in1)):
                basis = (in1,in2)
                break
            else:
                print("Your basis must be 90 degrees apart!")
        break
basis1 = basis[0]
basis2 = basis[1]
basis = (basis1,basis2)
while(True):
    try:
        binary1 = int(input("Input a binary string, this will act as the message\n"), 2)
        break
    except ValueError:
        print("Try Again! String must be in binary format (ex. 10110011)")
print("\n\n-----------------------------------------------------\n\n")

messagetosend = format(binary1, 'b')

arot = int(input("What is Alices secret rotation (in degrees)\n"))%360
brot = int(input("What is Bob's secret rotation (in degrees)\n"))%360
arads = math.radians(arot)

asecretrot = numpy.array(
[[math.degrees(math.cos(arads)),-math.degrees(math.sin(arads))],
[math.degrees(math.sin(arads)),math.degrees(math.cos(arads))]])

brads = math.radians(brot)
bsecretrot = numpy.array(
[[math.degrees(math.cos(brot)),-math.degrees(math.sin(brot))],
[math.degrees(math.sin(brot)),math.degrees(math.cos(brot))]])

def sendbit(bit):
    print("Sending: "+bit)
    tosend = numpy.array([math.degrees(math.cos(math.radians(int(basis1) + (90 * int(bit))))),math.degrees(math.sin(math.radians(int(basis1) + (90 * int(bit)))))])
    print("Sending "+ str(tosend.tolist()))
    amessage = aliceone(asecretrot, tosend)

    print ("Sending " + str(amessage.tolist())+ " to Bob")
    abmessage = bobone(bsecretrot, amessage)
    print("Sending "+ str(abmessage.tolist())+" to Alice")
    bmessage = alicetwo(asecretrot, abmessage)
    print("Sending "+ str(bmessage.tolist())+" to Bob")
    message = bobtwo(bsecretrot,bmessage)
    print("The recieved bit is " + str(message.tolist()))
    print(numpy.allclose(tosend,message))

def aliceone(secret,qubit):
    print("Applying Alice's secret...")
    return  numpy.dot(qubit,secret)
def bobone(secret, qubit):
    print("Applying Bob's secret...")
    return numpy.dot(qubit,secret)
def alicetwo(secret,qubit):
    print("Applying Alice's transposed secret...")
    return  numpy.dot(qubit,secret.T)
def bobtwo(secret,qubit):
    print("Applying Bob's transposed secret...")
    return  numpy.dot(qubit,secret.T)



for c in messagetosend:
    sendbit(c)
