import queue


def jump_2(nums):
    queue = []
    queue.append([0]) 
    i = 0
    while len(queue)> 0:
        x = queue.pop(0)
        
        for j in range(len(x)):
            temp = [k for k in range(x[j]+1, x[j]+1 + nums[x[j]] )]
            if len(nums)-1 in temp:
                return i+1
            queue.append(temp)
        i  +=1

    
    

if __name__ == "__main__":
    nums = [1,2,1,1,1]
    nums= [2,3,1,1,4]
    nums = [2,1,1,1,1]
    a = [k for k in range(1,3)]
    # print(a)
    print(jump_2(nums))