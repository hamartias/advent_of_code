import collections

realf = "input.txt"
testf = "test.txt"
def get_input(filename):
    numbers = []
    with open(filename) as f:
        for l in f:
            numbers.append(int(l.rstrip()))
    return numbers

def two_sum(num, iterable):
    comps = set()
    for n in iterable:
        comps.add(abs(num - n))
    for n in iterable:
        if n in comps:
            return True
    return False

def get_answer_partone(nums, preamble_length):
    deq = collections.deque([],preamble_length)
    for i in range(preamble_length):
        deq.append(nums[i])
    
    for i in range(preamble_length, len(nums)):
        if not two_sum(nums[i], deq):
            return nums[i]
        deq.append(nums[i])


def get_answer_parttwo(nums, num):
    
    def _helper(start_index):
        if start_index == len(nums)-1:
            return False
        have = nums[start_index]
        used = [have]
        while have < num:
            start_index += 1
            have += nums[start_index]
            used.append(nums[start_index])
        return have == num, min(used), max(used)

    for i in range(len(nums)-1):
        works, minu, maxu = _helper(i)
        if works:
            return minu+maxu

def main():
    nums = get_input(realf)
    num = get_answer_partone(nums, 25)
    final = get_answer_parttwo(nums, num)
    print(final)

if __name__ == "__main__":
    main()
