# import numpy as np
# processes = np.array(['P0','P1','P2','P3','P4'])

# available = np.array([3,3,2])

# max_demand =np.array([
#     [7, 5, 3],
#     [3, 2, 2],
#     [9, 0, 2],
#     [2, 2, 2],
#     [4, 3, 3]
# ])

# allocation = np.array([
#     [0, 1, 0],
#     [2, 0, 0],
#     [3, 0, 2],
#     [2, 1, 1],
#     [0, 0, 2]
# ])

# def can_allocate(process_need,work):
#     return all(need<=available for need,available in zip(process_need,work))

# def is_safe(processes,available,max_demand,allocation):
#     n = len(processes)
#     m = len(available)
#     need = max_demand-allocation
#     finish = [False]*n
#     safe_sequence=[]
#     work = available.copy()
#     # print(need)

#     while len(safe_sequence)<n:
#         progress = False
#         for i in range(n):
#             if not finish[i] and can_allocate(need[i],work):

#               for j in range(m):  
#                  work[j]+=allocation[i][j]
#               finish[i] = True
#               safe_sequence.append(processes[i])
#               progress=True
#               break
#         if not progress:
#                 return False,[]
#     return True,safe_sequence

# is_safe_sequence,safe_sequence = is_safe(processes,available,max_demand,allocation)

# if is_safe_sequence:
#     print("proceess : ")
#     print("Sequence is ","->".join(safe_sequence))
# else:
#     print("incorrect")
available = [3,3,2]
import numpy as np
max_demand =[
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]
allocation =[
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]
process = ['P0','P1','P2','P3','P4']
n = len(process)
m = len(available)
finish = [False]*n
work = available.copy()
safe_sequence = []
need = [[max_demand[i][j]-allocation[i][j] for j in range(3)] for i in range(5)]
# for row in need:
    #  print(row)

def can_allocate(process_need,work):
     return all(need<=available for need,available in zip(process_need,work))

def issafe(process):
 while len(safe_sequence)<n:
  progress  = False
  for i in range(n):
     if not finish[i] and can_allocate(need[i],work):
          for j in range(m):
               work[j]+=allocation[i][j]
          finish[i] =True
          safe_sequence.append(process[i])
          progress=True
          break
  if not progress:
          return False,safe_sequence
 return True,safe_sequence

safe,safe_sequences = issafe(process)
print("Safe Sequence is ","->".join(safe_sequence))     