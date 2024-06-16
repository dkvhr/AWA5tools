import sys

bin_file = sys.argv[1]
bin = open(bin_file, 'r')
bin = bin.read()

ops = {
        0x0 : 'nop',
        0x1 : 'prn',
        0x2 : 'pr1',
        0x3 : 'red',
        0x4 : 'r3d',
        0x5 : 'blo', #s8
        0x6 : 'sbm', #u5
        0x7 : 'pop',
        0x8 : 'dpl',
        0x9 : 'snr', #u5
        0xa : "mrg",
        0xb : '4dd',
        0xc : 'sub',
        0xd : 'mul',
        0xe : 'div',
        0xf : 'cnt',
        0x10 : 'lbl', #u5
        0x11 : 'jmp', #u5
        0x12 : 'eql',
        0x13 : 'lss',
        0x14 : 'gr8',
        0x1f : 'trm',
}

bit_counter = 0
opcode = ""
opcodes = []
i = 0
while i < len(bin):
    opcode += bin[i]
    bit_counter += 1
    if bit_counter == 5:
        opcodes.append(int(opcode, 2))
        if int(opcode, 2) == 0x5:
            opcode = ''
            for j in range(8):
                opcode += bin[i+j+1]
            i += 8
            opcodes.append(int(opcode, 2))
        bit_counter = 0
        opcode = ''
    i += 1

double_opcodes = [0x5, 0x6, 0x9, 0x10, 0x11]

i=0
while i < len(opcodes):
    instruction = ops.get(opcodes[i])
    print(instruction, end=' ')
    if opcodes[i] in double_opcodes:
        i += 1
        print(opcodes[i])
    else:
        print()
    i += 1
