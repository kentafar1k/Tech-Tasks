def inner():
    yield from (i * 2 for i in [1, 2, 3])
    yield "Done"

def outer():
    yield "Start"
    yield from inner()
    yield "End"

print(list(outer()))