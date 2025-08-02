def continued_frac(den, num):
    if num < den:
        raise ValueError("Numerator must be greater than or equal to denominator.")

    tmp = 0
    part = num // den
    cd = den
    cn = num % den
    res = [part]

    while cn != 1:
        part = cd // cn
        tmp = cd
        cd = cn
        cn = tmp % cn
        res.append(part)

    res.append(cd)
    return res
