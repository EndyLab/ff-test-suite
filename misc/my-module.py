## this is a comment
teststring = 'test true';
if type(teststring) == str:
    print (teststring);
else:
    print ('test false');

## testing string functions
s = 'abcba';
print (s.count('b'));
print (s.index('b'));
print (len(s));
print (str.capitalize(s));

## testing float functions
import random;
from decimal import Decimal;

for x in range(1):
  a = random.uniform(1,101);
  b = Decimal(a);
  print (type(a) == float);
  print (b);
  print (round(b, 3));
  print (float.as_integer_ratio(a));
