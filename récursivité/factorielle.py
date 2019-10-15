def factorielle(n):
    return (n* factorielle(n), n)[n > 2] 