days = int(input())
year = days//365
days %= 365
month = days//30
days %= 30
print(f'''{year} ano(s)
{month} mes(es)
{days} dia(s)''')
