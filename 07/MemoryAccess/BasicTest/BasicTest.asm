\\ push constant 10
@10
D=A
@SP
A=M
M=D
@SP
M=M+1

\\ pop local 0
@SP
M=M-1
@SP
A=M
D=M
@0
D=A
@LCL
A=M
D=D+A
A=D
M=D

\\ push constant 21
@21
D=A
@SP
A=M
M=D
@SP
M=M+1

\\ push constant 22
@22
D=A
@SP
A=M
M=D
@SP
M=M+1

\\ pop argument 2

\\ pop argument 1

\\ push constant 36
@36
D=A
@SP
A=M
M=D
@SP
M=M+1

\\ pop this 6

\\ push constant 42
@42
D=A
@SP
A=M
M=D
@SP
M=M+1

\\ push constant 45
@45
D=A
@SP
A=M
M=D
@SP
M=M+1

\\ pop that 5

\\ pop that 2

\\ push constant 510
@510
D=A
@SP
A=M
M=D
@SP
M=M+1

\\ pop temp 6
@SP
M=M-1
@SP
A=M
D=M
@11
M=D

\\ push local 0
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

\\ push that 5
@5
D=A
@THAT
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

\\ C_ARITHMETIC
arithmetic
\\ push argument 1
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

\\ C_ARITHMETIC
arithmetic
\\ push this 6
@6
D=A
@THIS
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

\\ push this 6
@6
D=A
@THIS
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

\\ C_ARITHMETIC
arithmetic
\\ C_ARITHMETIC
arithmetic
\\ push temp 6
@11
D=M
@SP
A=M
M=D
@SP
M=M+1

\\ C_ARITHMETIC
arithmetic
