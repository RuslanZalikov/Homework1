
def doesBrickFit(a, b, c, w, h):
    data = [a, b, c]
    data.pop(data.index(max(data)))
    return min(data) <= min(w,h) and max(data) <= max(w,h)

print(doesBrickFit(1, 2, 2, 1, 1))