def solution(ineq, eq, n, m):
    op = ineq+eq
    if op == ">=":
        return 1 if n>=m else 0
    elif op == "<=":
        return 1 if n<=m else 0
    elif op == ">!":
        return 1 if n>m else 0
    elif op == "<!":
        return 1 if n<m else 0