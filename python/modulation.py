import winsound
code='011001010110011001100110010110100110010101011010011001010101011001100110010101010110010101100110'
i=0
while i < len(code):
    if code[i] == '1':
        winsound.Beep(25000, 100)
    if code[i] == '0':
        winsound.Beep(20000, 100)
    i = i+1








