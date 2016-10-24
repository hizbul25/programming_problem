m = int(input())
m_set = [int(temp_m) for temp_m in input().strip().split(' ')]

n = int(input())
n_set = [int(temp_n) for temp_n in input().strip().split(' ')]

result = set(m_set) ^ set(n_set)
print(*sorted(result), sep='\n')


