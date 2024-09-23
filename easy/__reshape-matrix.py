# Write a Python function that reshapes a given matrix into a specified shape.
# Problem No.3
# contributed by Vivek Sharma
import numpy as np
def reshape_matrix(a:list[list[int|float]],new_shape: tuple[int|float]) -> list[list[int|float]]:
    return np.array(a).reshape(new_shape).tolist()
def main():
    a=[[1,2,3,4],[5,6,7,8]]
    new_shape = (4,2)
    ans=reshape_matrix(a,new_shape)
    print(ans)
if __name__ == "__main__":
    main() 