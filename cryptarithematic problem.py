import random

def check(S, E, N, D, M, O, R, Y):
    SEND = 1000*S + 100*E + 10*N + D
    MORE = 1000*M + 100*O + 10*R + E
    MONEY = 10000*M + 1000*O + 100*N + 10*E + Y

    return SEND + MORE == MONEY

def solve():
    while True:
        digits = random.sample(range(10), 8)  
        S, E, N, D, M, O, R, Y = digits

        if S != 0 and M != 0:  
            if check(S, E, N, D, M, O, R, Y):
                SEND = 1000*S + 100*E + 10*N + D
                MORE = 1000*M + 100*O + 10*R + E
                MONEY = 10000*M + 1000*O + 100*N + 10*E + Y
                return SEND, MORE, MONEY

SEND, MORE, MONEY = solve()

print(f'SEND = {SEND}')
print(f'MORE = {MORE}')
print(f'MONEY = {MONEY}')
