file = open("input13.txt").read().strip()
lines = file.split('\n')

ans = 0
alla = []
allb = []
alltarget = []
for line in lines:
    line = line.strip()
    line = line.split(':')
    if 'Button A' in line[0]:
        xa = int(line[1].split(',')[0].split('+')[1])
        ya = int(line[1].split(',')[1].split('+')[1])
        alla.append([xa,ya])
    if 'Button B' in line[0]:
        xb = int(line[1].split(',')[0].split('+')[1])
        yb = int(line[1].split(',')[1].split('+')[1])   
        allb.append([xb,yb])
    if 'Prize' in line[0]:
        xtarget = int(line[1].split(',')[0].split('=')[1])
        ytarget = int(line[1].split(',')[1].split('=')[1])
        alltarget.append([xtarget,ytarget])



ans = 0
target_diff = 10000000000000
for i in range(len(alla)):
    xa, ya = alla[i]
    xb, yb = allb[i]
    xtarget, ytarget = alltarget[i]
    xtarget += target_diff
    ytarget += target_diff

    det = xb*ya - xa*yb
    assert(det!=0)
    num1 = -(xtarget*yb - xb*ytarget)
    num2 = -(-xtarget*ya + xa*ytarget)
    if(num1%det!=0): continue
    if(num2%det!=0): continue
    x0 = num1//det
    x1 = num2//det

    ans += x0*3+x1

print(ans)