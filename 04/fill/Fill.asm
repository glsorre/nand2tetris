// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
  @8192
  D=A
  @index
  M=D // Initialize pixel index to 8192 at RAM[17]

(LOOP)
  @KBD
  D=M
  @PRESSED
  D;JNE   // goto PRESSED if KBD not equal to 0
  @UNPRESSED
  D;JEQ   // goto UNPRESSED if KBD equal to 0
  @LOOP
  0;JMP // loop if UNPRESSED

(UNPRESSED)
  @8192
  D=A
  @index
  M=D // Initialize pixel index to 8192 at RAM[17]
  @WHITE_LOOP
  0;JMP

(PRESSED)
  @8192
  D=A
  @index
  M=D // Initialize pixel index to 8192 at RAM[17]
  @BLACK_LOOP
  0;JMP

(BLACK_LOOP)
  @LOOP
  D;JLT
  @SCREEN
  A=A+D   // Calculate byte address
  M=-1    // Fill with black
  D=D-1
  @BLACK_LOOP
  0;JMP   // goto END

(WHITE_LOOP)
  @LOOP
  D;JLT
  @SCREEN
  A=A+D   // Calculate byte address
  M=0   // Fill with black
  D=D-1
  @WHITE_LOOP
  0;JMP   // goto END