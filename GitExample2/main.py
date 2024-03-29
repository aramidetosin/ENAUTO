def ip_to_binary_convrter(ip):
    ip_split = ip.split(".")

    ip_binary = [bin(int(i))[2:] for i in ip_split]
    ip_padding = []

    for i in ip_binary:
        i_string =str(i)
        if len(i_string) < 8:
            y = 8-len(i_string)
            new_i = "0"*y+i_string
            ip_padding.append(new_i)
        else:
            ip_padding.append(i_string)
    return ".".join(ip_padding)

if __name__ == "__main__":
    ip = "192.168.10.1"
    print(ip_to_binary_convrter(ip))