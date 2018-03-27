\\ push constant 3030
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1

\\ pop pointer 0

\\ push constant 3040
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1

\\ pop pointer 1

\\ push constant 32
@32
D=A
@SP
A=M
M=D
@SP
M=M+1

\\ pop this 2

\\ push constant 46
@46
D=A
@SP
A=M
M=D
@SP
M=M+1

\\ pop that 6

\\ push pointer 0

\\ push pointer 1

\\ C_ARITHMETIC
arithmetic
\\ push this 2
