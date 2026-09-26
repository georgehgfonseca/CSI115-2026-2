# Escreva uma funcao que recebe uma lista de inteiros e 
# retorna outra lista contendo apenas os inteiros positivos
def filter_positive(nums: list[int]) -> list[int]:
    postive_nums = []

    for i in range(len(nums)):
        if nums[i] > 0:
            postive_nums.append(nums[i])

    return postive_nums

def filter_positive_while(nums: list[int]) -> list[int]:
    postive_nums = []

    i = 0
    while i < len(nums):
        if nums[i] > 0:
            postive_nums.append(nums[i])
            
        i += 1

    return postive_nums


nums = [4, 0, -2, 5, 6, -7]
print(filter_positive(nums)) # [4, 5, 6]