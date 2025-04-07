def makeTriangle(sign):
    def triangle(n):
        res = ""
        for i in range(1, n+1):
            res += i * sign + "\n"
        return res
    return triangle

print(makeTriangle("*")(5))
print(makeTriangle("@")(2))
print(makeTriangle("0")(1))
