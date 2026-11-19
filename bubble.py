check_count = 0

def bubble(nums, count=0):

    global check_count

    # MAX LOOP
    if count >= len(nums) - 1:
        return nums

    swapped = False
    i = 0
    # while i < len(nums) - 1:
    while i < len(nums) - count - 1:
        check_count += 1
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            swapped = True
        i += 1

    # NO MORE TO SORT
    if not swapped:
        return nums

    # RECURSIVE
    return bubble(nums, count+1)

nums = [8, 3, 9, 2, 1, 4, 7, 92, 56, 22, 31, 78, 0]
# nums = [1,2,3,4,5,6,7,0]
print(f"BEFORE: {nums} ")

nums = bubble(nums)
print(f"AFTER : {nums} checked count={check_count}")

