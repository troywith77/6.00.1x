def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    funcs = []

    def foo(n, k):
        def bar(x):
            return n * x ** k
        return bar

    for i in range(len(L)):
        funcs.append(foo(L[i], len(L) - 1 - i))

    def sumUp(x):
        result = 0
        for f in funcs:
            result += f(x)
        return result

    return sumUp

print(general_poly([1, 2, 3, 4])(10))