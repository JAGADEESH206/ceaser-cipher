def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            offset = (ord(char) - start + shift) % 26 if mode == "encrypt" else (ord(char) - start - shift) % 26
            result += chr(start + offset)
        else:
            result += char
    return result


def is_numerical(text):
    try:
        float(text)
        return True
    except ValueError:
        return False


# ------------------- UI & Printing Helpers -------------------

def print_colored(message, color="green", bold=True):
    colors = {
        "green": "32",
        "cyan": "36"
    }
    color_code = colors.get(color, "32")
    style = "\033[1m" if bold else ""
    reset = "\033[0m"
    print(f"\033[{color_code}m{style}{message}{reset}")


def print_line():
    print("=" * 56)


def print_menu():
    print_line()
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Brute Force Decryption")
    print("4. Exit")
    print_line()


def print_goodbye():
    print_colored("GOODBYE!!", color="cyan")
    print_line()


# ------------------- User Input Handlers -------------------

def get_mode():
    while True:
        print_colored("\nEnter mode [1/2/3/4]:")
        choice = input("> ").strip().lower()
        if choice not in ["1", "2", "3", "4"]:
            print_colored("Invalid mode!", color="cyan")
        else:
            return choice


def get_message():
    while True:
        print_colored("\nEnter your message:")
        text = input("> ")
        if is_numerical(text):
            print_colored("The message can't be a number!", color="cyan")
        else:
            return text


def get_shift():
    while True:
        print_colored("\nEnter the shift:")
        shift = input("> ")
        if not shift.isdigit():
            print_colored("Shift must be a digit!", color="cyan")
        elif int(shift) < 1:
            print_colored("Shift must be greater than 0!", color="cyan")
        else:
            return int(shift)


# ------------------- Cipher Tools -------------------

def brute_force_decrypt(text):
    print_line()
    print_colored("\nBRUTE FORCE DECRYPTION", color="cyan")
    print()
    for shift in range(1, 26):
        output = caesar_cipher(text, shift, mode="decrypt")
        print_colored(f"Shift {shift:2}:", color="green")
        print(output)
        print()
    print_line()


# ------------------- Main Program -------------------

def main():
    while True:
        print_menu()
        choice = get_mode()

        if choice == "4":
            print()
            print_goodbye()
            break

        text = get_message()

        if choice in ["1", "2"]:
            shift = get_shift()
            mode = "encrypt" if choice == "1" else "decrypt"
            label = "Encrypted Message" if mode == "encrypt" else "Decrypted Message"
            result = caesar_cipher(text, shift, mode)
            print()
            print_colored(f"{label}:", color="green")
            print(result)
        else:
            brute_force_decrypt(text)

        print_colored("\nEncrypt/Decrypt Again? (y/n):")
        again = input("> ").strip().lower()
        print()

        if again not in ("yes", "y"):
            print_goodbye()
            break


if __name__ == "__main__":
    main()
