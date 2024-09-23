# Implementation of Relu Activation function
# Problem No.42
# contributed by Vivek Sharma

def relu(z:float)-> float:
    return max(0,z)

def main():
    z=4
    ans=max(0,z)
    print(ans)

if __name__=='__main__':
    main()