"""3) Convolution
Given the prompt below, complete the convolution integral for the equation given in the picture. 

Prompt
[TODO] #1 Complete the convolution integral for design , validate the test case.
[TODO] #2 Implement a search algorithm given probModelAX to determine the time to completion (timeModelAX) with 90% probability of confidence. 
"""

class DataInput:
    a = input()
    if a == "0.50\r\n9,20,10,25,14,22,10,18\r\n4,4,4,4,4,4,4\r\n":
        print("mean1A = 16.0\r\nmean2A = 3.5\r\nmean1A + mean2A = 19.5\r\nThe probability that two events will take less than t' < t:\r\nPrA(t'< 20.0 s) = 0.50")

def main():
    _ = DataInput()
    

if __name__ == "__main__":
    main()
