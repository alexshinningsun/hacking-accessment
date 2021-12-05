from secert import flag  # you cannot get the flag because it's secret
assert flag.startswith("flag{")
assert flag.endswith("}")
assert len(flag)==22

def lfsr(R,mask):
    # shift left
    output = (R << 1) & 0xffffffffffffffff
    # mask
    i=(R&mask)&0xffffffffffffffff
    # calculate the lastbit
    lastbit=0
    while i!=0:
        lastbit^=(i&1)
        i=i>>1
    # append the lastbit to the shifted value
    output^=lastbit
    # return the new value and the lastbit
    return (output,lastbit)

R=int(flag[5:-1],16)
mask = 0b1010010000001000000010001001010010100100000010000000100010010100

# the bits output by Linear Shift Feedback Register
# will be write to 'key' file
f=open("key","w")
for i in range(100):
    tmp=0
    for j in range(8):
        (R,out)=lfsr(R,mask)
        tmp=(tmp << 1)^out
    f.write(chr(tmp))
f.close()
