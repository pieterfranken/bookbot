def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

def get_words():
    count = 0
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()
    print(words)
    for word in words:
        count += 1
    print(count)

def count_characters(file_path):
    # Initialize counts for each letter to zero
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    count_e = 0
    count_f = 0
    count_g = 0
    count_h = 0
    count_i = 0
    count_j = 0
    count_k = 0
    count_l = 0
    count_m = 0
    count_n = 0
    count_o = 0
    count_p = 0
    count_q = 0
    count_r = 0
    count_s = 0
    count_t = 0
    count_u = 0
    count_v = 0
    count_w = 0
    count_x = 0
    count_y = 0
    count_z = 0

    # Open the file and read its contents
    with open(file_path, 'r') as f:
        text = f.read().upper()  # Read and convert to uppercase

    # Count occurrences of each letter
    for char in text:
        if char == 'A':
            count_a += 1
        elif char == 'B':
            count_b += 1
        elif char == 'C':
            count_c += 1
        elif char == 'D':
            count_d += 1
        elif char == 'E':
            count_e += 1
        elif char == 'F':
            count_f += 1
        elif char == 'G':
            count_g += 1
        elif char == 'H':
            count_h += 1
        elif char == 'I':
            count_i += 1
        elif char == 'J':
            count_j += 1
        elif char == 'K':
            count_k += 1
        elif char == 'L':
            count_l += 1
        elif char == 'M':
            count_m += 1
        elif char == 'N':
            count_n += 1
        elif char == 'O':
            count_o += 1
        elif char == 'P':
            count_p += 1
        elif char == 'Q':
            count_q += 1
        elif char == 'R':
            count_r += 1
        elif char == 'S':
            count_s += 1
        elif char == 'T':
            count_t += 1
        elif char == 'U':
            count_u += 1
        elif char == 'V':
            count_v += 1
        elif char == 'W':
            count_w += 1
        elif char == 'X':
            count_x += 1
        elif char == 'Y':
            count_y += 1
        elif char == 'Z':
            count_z += 1

    # Print the results
    print(f"A: {count_a}")
    print(f"B: {count_b}")
    print(f"C: {count_c}")
    print(f"D: {count_d}")
    print(f"E: {count_e}")
    print(f"F: {count_f}")
    print(f"G: {count_g}")
    print(f"H: {count_h}")
    print(f"I: {count_i}")
    print(f"J: {count_j}")
    print(f"K: {count_k}")
    print(f"L: {count_l}")
    print(f"M: {count_m}")
    print(f"N: {count_n}")
    print(f"O: {count_o}")
    print(f"P: {count_p}")
    print(f"Q: {count_q}")
    print(f"R: {count_r}")
    print(f"S: {count_s}")
    print(f"T: {count_t}")
    print(f"U: {count_u}")
    print(f"V: {count_v}")
    print(f"W: {count_w}")
    print(f"X: {count_x}")
    print(f"Y: {count_y}")
    print(f"Z: {count_z}")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
get_words()
count_characters("books/frankenstein.txt")
