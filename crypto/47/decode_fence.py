def decode_fence(encoded_message, rails=2):
    if rails <= 1 or rails >= len(encoded_message):
        return encoded_message

    # Mark zigzag positions for each character in the plaintext order.
    pattern = [[False for _ in encoded_message] for _ in range(rails)]
    row = 0
    step = 1
    for col in range(len(encoded_message)):
        pattern[row][col] = True
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        row += step
    print("Zigzag Pattern:")
    for r in pattern:
        print(r)

    # Fill the marked positions row by row using the ciphertext.
    decoded_grid = [["" for _ in encoded_message] for _ in range(rails)]
    index = 0
    for r in range(rails):
        for c in range(len(encoded_message)):
            if pattern[r][c]:
                decoded_grid[r][c] = encoded_message[index]
                index += 1
    print("\nDecoded Grid:")
    for r in decoded_grid:
        print(r)

    # Read characters following the zigzag traversal to recover plaintext.
    decoded_message = []
    row = 0
    step = 1
    for col in range(len(encoded_message)):
        decoded_message.append(decoded_grid[row][col])
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        row += step
    print(f"\nDecoded Message:", decoded_message)
    
    return "".join(decoded_message)

if __name__ == "__main__":
    encoded_message = "fa{fe13f590lg6d46d0d0}"
    original_message = decode_fence(encoded_message)
    print(original_message.lower())
