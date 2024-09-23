# Implementation of Log softmax function
# Problem No.39
# contributed by Vivek Sharma
import numpy as np
def log_softmax(scores:list) -> np.ndarray:
    scores = scores - np.max(scores)
    ans= scores - np.log(np.sum(np.exp(scores)))
    return ans
def main():
    A = np.array([1,2,3])
    ans = log_softmax(A)
    print(ans)
if __name__ == '__main__':
    main()

