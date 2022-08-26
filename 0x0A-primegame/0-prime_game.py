#!/usr/bin/python3
"""
This module returns the winner of a prime number game after several rounds
"""


def checkForprime(L):
    """
    This function checks for prime numbers in a list
    """

    for num in L:
        if (num > 1) and (len(L) > 1):
            if num == 2:
                break
                return 1
            elif num % 2 != 0:
                break
                return 1
            else:
                return 0
        else:
            return 0


def isWinner(x, nums):
    """
    This function returns the winner of a prime number game
    """

    playerA = 0
    playerB = 0
    rounds = 1

    for round_num in range(x):
        prime_num_to = nums[round_num]
        prime_num_list = [i + 1 for i in range(prime_num_to)]

        while (checkForprime(prime_num_list)) == 1:
            for number in prime_num_list:
                if ((number != 1) and ((number % 2) != 0)) or (number == 2):
                    primeN = number
                    prime_num_list.remove(number)

                    for multiples in prime_num_list:
                        if ((multiple % primeN) == 0):
                            M = multiple
                            prime_num_list.remove(M)

                    if rounds % 2 == 0:
                        playerB += 1
                    else:
                        playerA += 1

                    rounds += 1
                    break

    if playerA > playerB:
        return "Maria"
    else:
        return "Ben"
