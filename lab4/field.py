def field(items, *args):
    assert len(args) > 0
    for j in items:
        if len(args) == 1:
            if j[args[0]] is not None:
                yield j[args[0]]
        else:
            ans = {}
            for i in args:
                if j[i] is not None:
                    ans[i] = j[i]
            if ans:
                yield ans


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}]

titles = list(field(goods, 'title'))  # ['Ковер', 'Диван для отдыха']
prices = list(
    field(goods, 'title', 'price'))  # [{'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}]

print(titles)
print(prices)
