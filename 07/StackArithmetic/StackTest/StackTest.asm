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
@TRUE2
D;JEQ
@SP
A=M
M=0
@END2
0;JMP
(TRUE2)
@SP
A=M
M=-1
(END2)
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
@TRUE5
D;JEQ
@SP
A=M
M=0
@END5
0;JMP
(TRUE5)
@SP
A=M
M=-1
(END5)
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
@TRUE8
D;JEQ
@SP
A=M
M=0
@END8
0;JMP
(TRUE8)
@SP
A=M
M=-1
(END8)
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
@TRUE11
D;JLT
@SP
A=M
M=0
@END11
0;JMP
(TRUE11)
@SP
A=M
M=-1
(END11)
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
@TRUE14
D;JLT
@SP
A=M
M=0
@END14
0;JMP
(TRUE14)
@SP
A=M
M=-1
(END14)
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
@TRUE17
D;JLT
@SP
A=M
M=0
@END17
0;JMP
(TRUE17)
@SP
A=M
M=-1
(END17)
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
@TRUE20
D;JGT
@SP
A=M
M=0
@END20
0;JMP
(TRUE20)
@SP
A=M
M=-1
(END20)
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
@TRUE23
D;JGT
@SP
A=M
M=0
@END23
0;JMP
(TRUE23)
@SP
A=M
M=-1
(END23)
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
@TRUE26
D;JGT
@SP
A=M
M=0
@END26
0;JMP
(TRUE26)
@SP
A=M
M=-1
(END26)
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

