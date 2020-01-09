import re

is_code_regex = re.compile(r"[a-zA-Z]+")
encrypt_text = input('Enter your encrypt text: ')
mo = is_code_regex.findall(encrypt_text)

mo_join = ''.join(mo).lower()

count_code = {}
for val in mo_join:
    if val in count_code:
        count_code[val] += 1
    else:
        count_code[val] = 1

all_count = sum(count_code.values())
count = 0
char_frequency = {
    'e':11.40962588,
    'a':8.446499792,
    't':8.184687661,
    'i':7.130098608,
    'o':7.051799653,
    's':6.973500697,
    'n':6.770412782,
    'r':6.222320096,
    'h':4.255058847,
    'l':3.87335144,
    'd':3.870904598,
    'c':3.195576109,
    'u':2.953338716,
    'm':2.671951846,
    'p':2.02353862,
    'f':1.984389146,
    'g':1.820450708,
    'y':1.793535443,
    'w':1.698108591,
    'b':1.644278059,
    'v':0.998311679,
    'k':0.8955443,
    'j':0.205534757,
    'x':0.176172649,
    'q':0.08319264,
    'z':0.078298955
    }
char_frequency_list = char_frequency.items()

for k, v in sorted(count_code.items(), key=lambda x: x[-1]):
    print(str(k)+ ' : ' + str(v) + ' : ' + str(float( int(v)/all_count * 100)))
    count += 1
