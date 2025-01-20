H,W,h,w = map(int,input().split())
h_re = int(((H-1) - (H-1)%(h+1))/(h+1))
w_re = int(((W-1) - (W-1)%(w+1))/(w+1))
print((h_re+1)*(w_re+1))