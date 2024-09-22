input_text = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2"
def swap_letters_in_blocks(text):
    # Ensure text length is a multiple of 3 by padding with spaces if needed
    while len(text) % 3 != 0:
        text += ' '
    
    result = []
    
    # Iterate through the string in blocks of 3 letters
    for i in range(0, len(text), 3):
        block = text[i:i+3]
        
        # Swap the first and third letters
        swapped_block = block[2] + block[0] + block[1]
        
        # Add the swapped block to the result
        result.append(swapped_block)
    
    # Join the result list into a single string
    return ''.join(result)

# Example usage

output = swap_letters_in_blocks(input_text)
print(output)
