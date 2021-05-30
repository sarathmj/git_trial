'''

Write a function check_sum(), which, given li, a list of integers, and num,
 whether any two numbers in li add up to num. There are no duplicates in li.
'''

def check_sum(li, k):
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[i] + li[j] == k:
                return True
    return False


'''
python split string function
'''

def split_string(str):
    op_str = []
    for x in range(0, len(str)):
        sec = x+2
        tri = x+3
        itr_2 = str[x:sec]
        if(len(itr_2) > 1):
            if(itr_2 not in op_str):
                op_str.append(itr_2)
            if(x+3 <= len(str)):
                iter_3 = str[x:tri]
                if(iter_3 not in op_str):
                    op_str.append(iter_3)
    return op_str