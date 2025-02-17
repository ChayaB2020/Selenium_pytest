
grid=['l']
new_grid=[]
for i in grid:
    new_grid.append(sorted(i))
#grid.sort()
column=[[sub[k] for sub in new_grid] for k in range(len(grid[0]))]
print(column)
for ele in column:
    if ele == sorted(ele):
        print(True)



  # Write your code here
   # grid.sort()
    #column=[[sub[k]for sub in grid]  for k in range(len(grid[0]))]
   # for ele in column:
       # if ele != sorted(ele):
        #    return False
   # return True