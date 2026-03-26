def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97

            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += new_char
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)


def main():
    print("===== File Encryption/Decryption Tool =====")
    print("1. Encrypt File")
    print("2. Decrypt File")

    choice = input("Enter your choice (1 or 2): ")

    filename = input("Enter the file name (e.g., example.txt): ")

    shift = int(input("Enter shift value (e.g., 3): "))

    try:
        content = read_file(filename)

        if choice == '1':
            encrypted_content = caesar_encrypt(content, shift)

            new_filename = "encrypted_" + filename

            write_file(new_filename, encrypted_content)

            print(f"✅ File successfully encrypted as: {new_filename}")

        elif choice == '2':
            decrypted_content = caesar_decrypt(content, shift)

            new_filename = "decrypted_" + filename

            write_file(new_filename, decrypted_content)

            print(f"✅ File successfully decrypted as: {new_filename}")

        else:
            print("❌ Invalid choice. Please select 1 or 2.")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename.")
    except ValueError:
        print("❌ Error: Shift must be a number.")


if __name__ == "__main__":
    main()