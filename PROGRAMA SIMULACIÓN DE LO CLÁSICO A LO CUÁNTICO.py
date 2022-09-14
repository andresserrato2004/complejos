import numpy as np

import math


def main():
    m1 = np.array([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]])
    n = int(input())
    result = np.dot(m1, m1)
    for i in range(n-1):
        result_f = np.dot(result,result)
        result = result_f
    print(result)



main()
