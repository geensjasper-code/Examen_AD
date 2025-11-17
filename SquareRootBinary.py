def square_root_bisection(base, margin=1e-6, MaxIter=1000):
    if base < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    # Set bounds
    if 0 < base < 1:
        LB, UB = 0, 1
    else:
        LB, UB = 0, base

    count = 0
    mid = (UB + LB) / 2  # initialize mid

    while UB - LB > margin and count < MaxIter:
        mid = (UB + LB) / 2

        if mid ** 2 > base:
            UB = mid
        else:
            LB = mid

        count += 1

    # Return the best approximation after loop ends
    return f"The square root of {base} is approximately {mid}"


# Examples
print(square_root_bisection(0.5, 0.0001, 10000))
print(square_root_bisection(9, 0.0001, 10000))
print(square_root_bisection(0.25, 0.0001, 10000))