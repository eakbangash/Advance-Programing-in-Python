# import numpy as np
# from numpy import random
# A = random.randint (10,size=[4,3])
# print (A)
# A = np.array(A)
# print( A.shape)
# B = random.randint(10,size=[1])
# print(B)
# B = np.array(B)
# print( B.shape)
# C = A*B
# print(C)
# print("shape after broadcasting: ", C.shape)

# import numpy as np
# from numpy import random
# A = random.randint (10,size=[2,4,3])
# print (A)
# B = random.randint(10,size=[4,3])
# print(B)
# C = A*B
# print(C)
# print("shape after broadcasting: ", C.shape)

#Failure Case for wrong shapes

# import numpy as np
# from numpy import random
# A = random.randint (10,size=[3,4])
# print(A)
# A = np.array(A)
# print( A.shape)
# B = random.randint(10,size=[2,3])
# print(B)
# B = np.array(B)
# print( B.shape)
# C = A*B
# print(C)
# print("shape after broadcasting: ", C.shape)

# import numpy as np
# from numpy import random
# A = random.randint (10,size=[2,4,3])
# print (A)
# B = random.randint(10,size=[3,2])
# print(B)
# C = A*B
# print(C)
# print("shape after broadcasting: ", C.shape)