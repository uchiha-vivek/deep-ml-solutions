# Implementation of Relu Activation function
# Problem No.44
# contributed by Vivek Sharma

def leaky_relu(z:float,alpha:float=0.01) -> float:
    if (z>0):
        return z
    else :
        return alpha*z
    
def main():
    z1=4
    z2=0
    z3=-0.5
    print(leaky_relu(z1))
    print(leaky_relu(z2))
    print(leaky_relu(z3))

if __name__ == "__main__":
    main()
    