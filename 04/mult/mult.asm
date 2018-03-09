// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
  @result   
  M=0     // Initialize result to RAM[16]
  @R1
  D=M
  @count
  M=D // Initialize count to RAM[16]
(LOOP)
  @count
  D=M
  @SETR2
  D;JEQ // IF count = to zero jump to SETR2
  @R0
  D=M // Set R0 to D
  @result
  M=D+M // Sum D to result
  @count
  M=M-1 // Decrement count
  @LOOP
  0;JMP // Repeat
(SETR2)   
  @result
  D=M
  @R2
  M=D // Write result to RAM[2]
  @END
  0;JMP     
(END)
  @END
  0;JMP
