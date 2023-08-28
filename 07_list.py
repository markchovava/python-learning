colors = ['red', 'white', 'blue']
print(colors)
# Add to list
colors.append('green')
print(colors)
colors[3] = 'black'
print(colors)

# Loop
for color in colors:
    print(color)

""" i = 0
for color in colors:
    if(not(color == 'blue')):
        print(f'{i} not it')
        i += 1
    else:
        print('Done')
        break
 """

print('----------------------')
for i in range(len(colors)):
    if colors[i] == 'white':
        print(f'{colors[i]} is the one.')
    else:
        print(colors[i])
