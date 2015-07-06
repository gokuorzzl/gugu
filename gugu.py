import sys

dan = input('몇단?:')
try:
    dan = int(dan)
except ValueError:
    dan = 0

if 2 <= dan <= 9:
    y = input('y는 얼마? :')
    try:
        y = int(y)
    except ValueError:
        print("오류입니다", file=sys.stderr)
        raise SystemExit()
    print(dan, '*', y, '=', dan*y)
else:
    for x in range(2, 10):
        for y in range(1, 10):
            print(x, '*', y, '=', x*y)