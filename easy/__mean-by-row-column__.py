# Implementation of Log softmax function
# Problem No.4
# contributed by Vivek Sharma


def calculate_matrix_mean(matrix:list[list[float]],mode:str) -> list[float]:
    if mode=='column':
        return [sum(col)/len(matrix) for col in zip(*matrix)]
    elif  mode=='row':
        return [sum(row)/len(row) for row in matrix ]
    else :
        raise ValueError("Mode must be  row or column ")
    
def main():
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    mode='column'
    ans = calculate_matrix_mean(matrix,mode)
    print(ans)

if __name__ == '__main__':
    main()