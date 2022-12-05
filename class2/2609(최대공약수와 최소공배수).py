import math

a, b = map(int, input().split())

gcd_ab = math.gcd(a, b)
lcd_ab = (a/gcd_ab * b/gcd_ab) * gcd_ab
print(math.gcd(a, b), int(lcd_ab))