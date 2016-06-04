# def recdf(v, w, is_take, i):
#     v += items[i][0] * is_take
#     w += items[i][1] * is_take
#     if w + items[i][1] * is_take > capacity:
#         print v, w
#         return
#     if i == len(items):
#         print v, w
#         return
#     recdf(v, w, 0, i + 1)
#     recdf(v, w, 1, i + 1)
#     return
