def containDupilcates(nums):
    hset= set()

    for i in nums:
        if i in hset:
            return True
        hset.add(i)
    return False


l = [1,2,1,4,6,8,2,8]

print(containDupilcates(l))
