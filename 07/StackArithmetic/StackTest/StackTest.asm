// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
A=M
A=A-1
A=A-1
D=M
A=A+1
D=D-M
@SP
M=M-1
M=M-1
@true.3
D;JEQ
@SP
A=M
M=0
@end.3
0;JMP
(true.3)
@SP
A=M
M=-1
(end.3)
@SP
M=M+1

// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
A=M
A=A-1
A=A-1
D=M
A=A+1
D=D-M
@SP
M=M-1
M=M-1
@true.6
D;JEQ
@SP
A=M
M=0
@end.6
0;JMP
(true.6)
@SP
A=M
M=-1
(end.6)
@SP
M=M+1

// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
A=M
A=A-1
A=A-1
D=M
A=A+1
D=D-M
@SP
M=M-1
M=M-1
@true.9
D;JEQ
@SP
A=M
M=0
@end.9
0;JMP
(true.9)
@SP
A=M
M=-1
(end.9)
@SP
M=M+1

// push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
A=M
A=A-1
A=A-1
D=M
A=A+1
D=D-M
@SP
M=M-1
M=M-1
@true.12
D;JLT
@SP
A=M
M=0
@end.12
0;JMP
(true.12)
@SP
A=M
M=-1
(end.12)
@SP
M=M+1

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
A=M
A=A-1
A=A-1
D=M
A=A+1
D=D-M
@SP
M=M-1
M=M-1
@true.15
D;JLT
@SP
A=M
M=0
@end.15
0;JMP
(true.15)
@SP
A=M
M=-1
(end.15)
@SP
M=M+1

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
A=M
A=A-1
A=A-1
D=M
A=A+1
D=D-M
@SP
M=M-1
M=M-1
@true.18
D;JLT
@SP
A=M
M=0
@end.18
0;JMP
(true.18)
@SP
A=M
M=-1
(end.18)
@SP
M=M+1

// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
A=M
A=A-1
A=A-1
D=M
A=A+1
D=D-M
@SP
M=M-1
M=M-1
@true.21
D;JGT
@SP
A=M
M=0
@end.21
0;JMP
(true.21)
@SP
A=M
M=-1
(end.21)
@SP
M=M+1

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
A=M
A=A-1
A=A-1
D=M
A=A+1
D=D-M
@SP
M=M-1
M=M-1
@true.24
D;JGT
@SP
A=M
M=0
@end.24
0;JMP
(true.24)
@SP
A=M
M=-1
(end.24)
@SP
M=M+1

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
A=M
A=A-1
A=A-1
D=M
A=A+1
D=D-M
@SP
M=M-1
M=M-1
@true.27
D;JGT
@SP
A=M
M=0
@end.27
0;JMP
(true.27)
@SP
A=M
M=-1
(end.27)
@SP
M=M+1

// push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 53
@53
D=A
@SP
A=M
M=D
@SP
M=M+1

// add
@SP
A=M
A=A-1
A=A-1
D=M
A=A+1
D=D+M
@SP
M=M-1
M=M-1
@SP
A=M
M=D
@SP
M=M+1

// push constant 112
@112
D=A
@SP
A=M
M=D
@SP
M=M+1

// sub
@SP
A=M
A=A-1
A=A-1
D=M
A=A+1
D=D-M
@SP
M=M-1
M=M-1
@SP
A=M
M=D
@SP
M=M+1

// neg
@SP
A=M
A=A-1
D=M
D=-D
@SP
M=M-1
@SP
A=M
M=D
@SP
M=M+1

// and
@SP
A=M
A=A-1
A=A-1
D=M
A=A+1
D=D&M
@SP
M=M-1
M=M-1
@SP
A=M
M=D
@SP
M=M+1

// push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1

// or
@SP
A=M
A=A-1
A=A-1
D=M
A=A+1
D=D|M
@SP
M=M-1
M=M-1
@SP
A=M
M=D
@SP
M=M+1

// not
@SP
A=M
A=A-1
D=M
D=!D
@SP
M=M-1
@SP
A=M
M=D
@SP
M=M+1

