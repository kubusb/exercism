# 00001 = wink
# 00010 = double blink
# 00100 = close your eyes
# 01000 = jump
# 10000 = Reverse the order of the operations in the secret handshake.

def commands(binary_str):
    result = []
    if binary_str == "00000":
        return result
    if binary_str[-1] == "1":
        result.append("wink")
    if binary_str[-2] == "1":
        result.append("double blink")
    if binary_str[-3] == "1":
        result.append("close your eyes")
    if binary_str[-4] == "1":
        result.append("jump")
    if binary_str[-5] == "1":
        return result[::-1]
    return result
