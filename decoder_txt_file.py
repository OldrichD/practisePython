def decode(message_file):
    """
    Decode a message from a file.

    Parameters:
    - message_file (str): Path to the file with the encoded message.

    Returns:
    - str: Decoded message.

    This function reads an encoded message from a text file, decodes it
    by selecting words corresponding to numbers from a triangular number series,
    and returns the decoded message as a string.
    """
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Extract words and corresponding numbers
    words_and_numbers = [line.strip().split(' ', 1) for line in lines]

    # Convert numbers to integers
    words_and_numbers = [(int(number), word) for number, word in words_and_numbers]

    # Sort the list based on the numbers
    words_and_numbers.sort()

    # Generate the numbers forming the triangular number series
    triangular_numbers = []
    current_sum = 0
    n = 1
    while current_sum < len(words_and_numbers):
        current_sum += n
        triangular_numbers.append(current_sum)
        n += 1

    # Extract the words corresponding to the triangular number series
    decoded_message = [word for number, word in words_and_numbers if number in triangular_numbers]

    # Join the words to form the decoded message
    decoded_message_str = ' '.join(decoded_message)

    return decoded_message_str

# Example usage
message_file = 'coding_qual_input.txt'
decoded_message = decode(message_file)
print(decoded_message)