import itertools

CONST = 'bcdfghjklmnpqrstvwxz'
VOWELS = 'aeiou'


def product(a, b, repeat):
    if repeat % 2 == 0:
        for i in itertools.product(a, b, repeat=repeat//2):
            yield i
    else:
        for i in itertools.product(b, a, repeat=repeat//2+1):
            if i[0] != b[0]:
                break
            yield i[1:]


def generate_answers(n):
    return itertools.chain(product(CONST, VOWELS, repeat=n),
                           product(VOWELS, CONST, repeat=n))


if __name__ == '__main__':
    for answer in generate_answers(int(input())):
        print(''.join(answer))
