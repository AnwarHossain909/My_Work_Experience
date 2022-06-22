a,b,c,d = map(int,input().split())
start_time = a*60 + b
end_time = c*60+d
res = end_time-start_time
if res<=0:
    res += 24*60
hour = res//60
minute = res%60
print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(hour,minute))
