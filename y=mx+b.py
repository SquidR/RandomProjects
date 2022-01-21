import matplotlib.pyplot as plt

# im really bad at stuff like this
# i dont reccomend putting the recursions at a 
# high ammount due to lag or a crash happening
# if it doesnt work in replit (hasnt been tested)
# just go to https://trinket.io/python3/ and put
# this code into there, it will work
print('Changelog 1.2')
print('-Fixed pretty much the entire thing')
print('-Added ability to change size of graph')
print('-Fixed B variable glitching out')
print('will add while true loop later but not rn')
import os
# i stole this :smiling_imp:
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
# stupid inputs :angry:
b1 = int(input('Bounding Area 1 (Reccomended to be a negative number): '))
b2 = int(input('Bounding Area 2 (Reccomended to be a positive number): '))

m = float(input('M: '))
b = int(input('B: '))
rec = int(input('Recursions (how high you want x to go\nthis number will be multiplied\nbased on if you used a decimal\nor not, for example using\n10 recursions with a decimal\nof 0.33, your ammount of recursions\nwill turn into 30): '))
newx = 0

xg, y = ([0], [b])

# make sure it dont go haywire
if rec << 1:
  if m == 0.25:
    rec = rec * 4
  if m == 0.33:
    rec = rec * 3
  if m == 0.1:
    rec = rec * 10
  if m == 0.5:
    rec = rec * 2
  if m == 0.75:
    rec = rec * 2.5
    
if m >= 1:
  if b <= 0:
    ynegative = True  
# make the graph chart thingy
for i in range(0, rec):
  newx += 1
  additive = m*newx
  newy = additive+b
  xg.append(newx)
  y.append(newy)

print(xg, y)
# hmmmm what do i show
bounds = [b1, b2]
clearConsole()
# draw graph
plt.figure()
plt.xlim((bounds[0], bounds[1]))
plt.ylim((bounds[0], bounds[1]))
plt.plot([0,0],[bounds[0], bounds[1]], linewidth=1, color='red' )
plt.plot([bounds[0],bounds[1]],[0,0], linewidth=1, color='red' )
plt.plot(xg,y, linewidth=2, color='blue')
plt.title(f'y = {m}x + {b}')
plt.grid()
plt.show()
