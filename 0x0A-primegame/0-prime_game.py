#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """
    Returns the name of the player that won the most rounds
    """
    def sieve(n):
        primes = [True for _ in range(n+1)]
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n+1, p):
                    primes[i] = False
            p += 1
        primes[0] = primes[1] = False
        return primes

    max_num = max(nums)
    primes = sieve(max_num)
    prime_counts = [0] * (max_num + 1)
    for i in range(2, max_num + 1):
        prime_counts[i] = prime_counts[i-1] + (1 if primes[i] else 0)

    Maria_score = Ben_score = 0
    for n in nums:
        if prime_counts[n] % 2 == 1:
            Maria_score += 1
        else:
            Ben_score += 1

    if Maria_score > Ben_score:
        return "Maria"
    elif Ben_score > Maria_score:
        return "Ben"
    else:
        return None
