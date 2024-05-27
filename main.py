password_hash = "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"
import hashlib

with open('C:\Projets\hacker-sha\\10k-most-common.txt', "r") as file:
    for line in file:
        line = line.strip()
        print(line)
        hash = hashlib.sha1(line.encode()).hexdigest()
        if hash == password_hash:
            print("Password found: " + line)
            break
    else:
        print("Password not found")
