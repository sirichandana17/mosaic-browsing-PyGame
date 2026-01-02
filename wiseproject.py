#INPUT
import array as arr
#import numpy as np

print("Enter the row and column number of motif ")
lt1 = [int(i) for i in input().split()]
rp ,cp =lt1[0], lt1[1]
print("Enter the elements into motif:")
l1= [[int(i) for i in input().split()] for i in range(0,rp)]
print("MOTIF")
print(l1)
print()

print("Enter the row and column number of mosaic ")
lt2= [int(i) for i in input().split()]
rq ,cq =lt2[0], lt2[1]
print("Enter the elements into mosaic:")
l2= [[int(i) for i in input().split()] for i in range(0,rq)]
print("MOSAIC")
print(l2)
print()

print("OUTPUT")
#OUTPUT

def find_motif(mosaic,motif):

    matches = 0

    for i in range(rq - rp + 1):
        for j in range(cq - cp + 1):
            match_found = True
            for x in range(rp):
                for y in range(cp):
                    if motif[x][y] != 0 and mosaic[i+x][j+y] != motif[x][y]:
                        match_found = False
                        break
                if not match_found:
                    break
            if match_found:
                matches += 1
                print(i+1,j+1)

    print(f"Total matches found: {matches}")


mosaic = l2

motif = l1

find_motif(mosaic, motif)

