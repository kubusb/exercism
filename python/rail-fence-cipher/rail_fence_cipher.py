def encode(message, rails):
    # Remove spaces from the message
    message = message.replace(" ", "")
    
    # Create a 2D list to represent the rails
    fence = [[None] * len(message) for _ in range(rails)]
    
    rail = 0
    direction = 1
    
    # Fill the fence with characters
    for i, char in enumerate(message):
        fence[rail][i] = char
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction = -direction
    
    # Read off the encoded message
    return ''.join(char for rail in fence for char in rail if char is not None)

def decode(encoded_message, rails):
    # Create a 2D list to represent the rails
    fence = [[None] * len(encoded_message) for _ in range(rails)]
    
    rail = 0
    direction = 1
    
    # Mark the positions in the fence
    for i in range(len(encoded_message)):
        fence[rail][i] = True
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction = -direction
    
    # Fill the marked positions with characters from the encoded message
    index = 0
    for rail in range(rails):
        for i in range(len(encoded_message)):
            if fence[rail][i] is True:
                fence[rail][i] = encoded_message[index]
                index += 1
    
    # Read off the decoded message
    rail = 0
    direction = 1
    decoded = []
    for i in range(len(encoded_message)):
        decoded.append(fence[rail][i])
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction = -direction
    
    return ''.join(decoded)
