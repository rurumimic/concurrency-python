from functional import seq

# [1, 2, 3, 4]
# [2, 4, 6, 8]
# [6, 8]
# 14

# result = seq(1, 2, 3, 4) \
#     .map(lambda x: x * 2) \
#     .filter(lambda x: x > 4) \
#     .reduce(lambda x, y: x + y)

result = (
    seq(1, 2, 3, 4)
    .map(lambda x: x * 2)
    .filter(lambda x: x > 4)
    .reduce(lambda x, y: x + y)
)

print(f'Results: {result}')

'''
Results: 14
'''
