# MSP Simulator

## Warnings:
- This is a very simple MSP simulator for assembly code.  
- The **Pygame** library was used for visualization. You need to install this Python library:  
  ```
  pip install pygame
  ```
- This is not an exact simulator. Most of the instructions are not included in this project.  
- Some of the included instructions are incomplete. (Some flag values are updated, while others are not.)  
- The execution time of the code differs from real execution.  
- In reality, most instructions are **2 bytes**, so the **Program Counter (PC)** is incremented by **2** after executing an instruction. However, in this simulator, the **PC** is incremented by **1**.  
- The memory implementation is very weak and needs improvement.  
- **Memory and Stack are separated.** The **Stack Pointer is not used**, but the Stack itself can be used. **Pop, push, and call operations are supported.**  
- You can construct a **byte array**, but you must use a **label** after that line.  
- Arrays are defined in the **code section**. Do not use the `.data` section. :)  
- **Code cannot be seen in memory.** Memory only includes **array values**.  
- **Interrupts are not supported.** (I tried to develop this code until I learned about interrupts.)  
- **Timers are not supported.**  
- There are some **special registers**. In real systems, they should not be used (e.g., the **accumulator**). However, the simulator does not use these registers for a specific purpose, so you need to be careful about this.  
- **Registers have limitless capacity.** Overflow does not occur.  
- Therefore, there is no difference between **MOV.W, MOV.B, and MOV**—all of them behave the same.  

### ⚠️ Summary:  
A code may work in this simulator, but **it is not guaranteed to work on a real microcontroller.**  

---

## What We Have:
Although there are **many missing or incorrect parts**, the simulator is **useful for basic operations**.  

### ✅ Supported Features:
- **Arithmetic operations**: Addition, subtraction, increment, and decrement.  
- **Logical operations**: AND, OR, BIS, XOR.  
- **Shift operations**: **RRA** and **RLA** are supported.  
- **CMP operation**: Updates **zero** and **negative** flags.  
- **Jump operations**: Most jump instructions are supported.  
- **MOV and memory read operations** are supported.  
- **Stack operations**: Push and Pop are supported.  
- **Function calls**: Call and RET operations are supported, allowing function implementation.  
- **Seven-segment display**: Controlled by **Port 1**.  
- **LEDs**: 16 LEDs are connected to **Port 1 and Port 2**.  
- **Stack visualization**: The value pointed to by the **Stack Pointer** is highlighted in **green**.  
- **Register values**: Can be viewed.  
- **Array support**: You can define and view array values in memory.  
- **Comments**: Lines starting with `;` are supported.  

### 🎯 Debugging Features:
- **You can set breakpoints by clicking on the code.**  
- **Navigation buttons:**  
  - **Up and Down buttons**: Scroll through the code.  
- **Execution buttons:**  
  - `>` : Executes one operation.  
  - `>|` : Executes operations until a breakpoint.  
  - `>>>` : Executes operations (ignores breakpoints).  
  - `||` : Stops execution.  
- **File operations:**  
  - You can enter a filename by clicking the **rectangular area**.  
  - **You MUST click the "Dosya Oku" button** to read the code file.  
- **Source code should only contain the main part.**  
- **An example code file is available.**  

---
