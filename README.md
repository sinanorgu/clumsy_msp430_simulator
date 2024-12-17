Warnings:  
  This is a very simple msp simulator for assembly code.  
  Pygame library was used for visulation. You need to download this python library. (pip install pygame)  
  This is not an exact simulator. Most of the instruction are not included in this project.    
  Also some of included instruction are not complete. (Some flag values are updated but some of them are not)  
  Execution time of code is different than real execution.  
  In reality, most of the instructions are 2 byte, so PC(program counter) is incremented by 2 after executing an instrcution. But in this simulator pc is incremented by 1.   
  Memory implementation is very weak. It needs to be updated.   
  Memory and Stack are seperated. Stak pointer is not used but Stack can be used. Pop, push and call operations is supported.   
  You can construct a byte array but you need to use a label after that line.  
  Also arrays are defined in code section. Do not use ".data" section :)  
  Codes cannot be seen in Memory. Memory includes only array values.  
  Interrupts is not supported. (I tried to develop this code until I learned interrupt)    
  Timer is not supported.  
  There is some special registers. In real systems, they should not be used (for example accumulator).   
  But simulator is not use these register for a spesific purpose. You need to be careful about this situation.  
  Registers has limitless capacity. Overflow is not occured.  
  Therefore there is no difference between mov.w, mov.b and mov . All of them is same.  
  SUMMARY: A code may work in simulator, but it is not guaranteed that it will work in real microcontroller.  
  
What we have:  
    Although there are lots of missing or incorrect parts, it is useful for basic operations.  
    Addition, substruction, increment, decrement operations are supported.  
    and, or, bis, xor operations are supported.  
    Shift operations are rra, rla are supported.  
    cmp operation updates zero and negative flag.   
    Therefore most of the jump operation is supported.  
    mov and memory read operations are supported.  
    Push and pop is supported.   
    call and ret operation is supported. A function can be writed.  
    There is a seven segment display. (controlled by port1)  
    There are 16 leds connected to port1 and port2.  
    In stack, the value which pointed by stack pointer has green color :)  
    Value of a register can be seen.  
    You can define array.  
    Array values can be seen in memeory.  
    ;comment line is supported.   
    YOU CAN PUT BREAKPOINT BY CLICKING CODE.   
    Up and down buttons can be used for move the code.  
    Button >   : Executes one operation  
    Button >|  : Executes operations until breakpoint  
    Button >>> : Executes operations (ignores breakpoint)  
    Button ||  : Stops execution  
    You can type filename by clicking the rectangular area.  
    YOU HAVE TO CLICK dosya oku BUTTON to read the code file.  
    Source code should be consist of only main part.  
    Example code file is available.   
    

    

