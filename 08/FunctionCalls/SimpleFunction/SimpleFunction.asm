// function SimpleFunction.test 2
(SimpleFunction.test)
@SP
A=M
M=0
@SP
M=M+1
@SP
A=M
M=0
@SP
M=M+1

// push local 0
@0
D=A
@LCL
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 1
@1
D=A
@LCL
A=M
D=D+A
A=D
D=M
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

// push argument 1
@1
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

// return 
@LCL
D=M
@endFrame
M=D
@5
D=D-A
A=D
D=M
@retAddr
M=D
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
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