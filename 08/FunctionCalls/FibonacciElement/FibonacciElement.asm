//  init
@256
D=A
@SP
M=D

// call Sys.init 0
@Sys.init
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(Sys.init)

// push argument 0
@0
D=A
@ARG
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push constant 2
@2
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
@true.5
D;JLT
@SP
A=M
M=0
@end.5
0;JMP
(true.5)
@SP
A=M
M=-1
(end.5)
@SP
M=M+1

// if-goto IF_TRUE
@SP
M=M-1
@SP
A=M
D=M
@IF_TRUE
D;JNE

// goto IF_FALSE
@IF_FALSE
0;JMP

// label IF_TRUE
(IF_TRUE)

// push argument 0
@0
D=A
@ARG
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// return 
@LCL
D=M
@endFrame
M=D
// endFrame = LCL 
@5
D=D-A
A=D
D=M
@retAddr
M=D
// retAddr = *endFrame - 5 
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
// ARG = pop() 
@ARG
D=M+1
@SP
M=D
// SP = ARG + 1
@endFrame
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D
@endFrame
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D
@endFrame
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D
@endFrame
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D
@retAddr
A=M
0;JMP
// label IF_FALSE
(IF_FALSE)

// push argument 0
@0
D=A
@ARG
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push constant 2
@2
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

// push argument 0
@0
D=A
@ARG
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push constant 1
@1
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

// return 
@LCL
D=M
@endFrame
M=D
// endFrame = LCL 
@5
D=D-A
A=D
D=M
@retAddr
M=D
// retAddr = *endFrame - 5 
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
// ARG = pop() 
@ARG
D=M+1
@SP
M=D
// SP = ARG + 1
@endFrame
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D
@endFrame
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D
@endFrame
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D
@endFrame
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D
@retAddr
A=M
0;JMP
