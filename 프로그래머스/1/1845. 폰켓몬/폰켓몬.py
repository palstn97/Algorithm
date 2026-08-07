def solution(nums):
    target = len(nums) // 2
    pocket_set = set(nums)
    
    if len(pocket_set) < target:
        answer = len(pocket_set)
    else:
        answer = target
        
    return answer