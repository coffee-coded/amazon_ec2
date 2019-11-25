import os


def inputs():
    ip = input("Public IP or DNS [REQUIRED]:")
    x = input("Username [ec2-user] : ")
    if x == "":
        username = "ec2-user"
    else:
        username = x
    x = input("Path to public key (pem) [./Default.pem]: ")
    if x == "":
        path = "./Default.pem"
    else:
        path = x
    cmd = "ssh -i " + path + " " + username + "@" + ip
    return cmd


def inputs_2():
    ip = input("Public IP or DNS [REQUIRED]: ")
    file_path = input("Path of the file to be uploaded [Required] : ")
    x = input("Username [ec2-user] : ")
    if x == "":
        username = "ec2-user"
    else:
        username = x
    x = input("Path to public key (pem) [./Default.pem]: ")
    if x == "":
        path = "./Default.pem"
    else:
        path = x
    x = input("Relative path of the file [~]: ")
    if x == "":
        rel_path = "~"
    else:
        rel_path = x
    cmd = "scp -i " + path + " " + file_path + " " + username + "@" + ip + ":" + rel_path
    return cmd


if __name__ == '__main__':
    print("""
    _______________      ______                            __
   / ____/ ____/__ \    / ____/___  ____  ____  ___  _____/ /_
  / __/ / /    __/ /   / /   / __ \/ __ \/ __ \/ _ \/ ___/ __/
 / /___/ /___ / __/   / /___/ /_/ / / / / / / /  __/ /__/ /_
/_____/\____//____/   \____/\____/_/ /_/_/ /_/\___/\___/\__/

                                          -by Coffee Coded
    """)
    x = int(input("1. Connect to your ec2-system \n2. Transfer files to your ec2-instance\n     Choose : "))
    if x == 1:
        os.system(inputs())
    else:
        os.system(inputs_2())
