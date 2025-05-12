def run_3bit_computer(registers, program):
    # Unpack initial register values
    A, B, C = registers
    instruction_pointer = 0
    output = []

    # Helper function to compute the value of a combo operand
    def combo_value(operand):
        if operand <= 3:  # Literal value 0 through 3
            return operand
        elif operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C
        elif operand == 7:
            raise ValueError("Operand 7 is reserved and invalid.")

    # Start executing the program
    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]

        # Execute based on opcode
        if opcode == 0:  # adv
            A = A // (2 ** combo_value(operand))
        elif opcode == 1:  # bxl
            B = B ^ operand
        elif opcode == 2:  # bst
            B = combo_value(operand) % 8
        elif opcode == 3:  # jnz
            if A != 0:
                instruction_pointer = operand
                continue  # Skip instruction pointer increment
        elif opcode == 4:  # bxc
            B = B ^ C
        elif opcode == 5:  # out
            output.append(combo_value(operand) % 8)
        elif opcode == 6:  # bdv
            B = A // (2 ** combo_value(operand))
        elif opcode == 7:  # cdv
            C = A // (2 ** combo_value(operand))
        else:
            raise ValueError(f"Unknown opcode: {opcode}")

        # Move to the next instruction (increment by 2)
        instruction_pointer += 2

    return ",".join(map(str, output))


# Example usage
initial_registers = (30118712, 0, 0)  # Values for registers A, B, C
program = [2,4,1,3,7,5,4,2,0,3,1,5,5,5,3,0]  # Program as a list of 3-bit opcodes and operands

result = run_3bit_computer(initial_registers, program)
print("Final Output:", result)
