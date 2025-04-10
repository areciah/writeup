def reverse_to_org(menu_str):
    org = 0
    for i in range(16):
        char = menu_str[i]
        if char == '_':
            res = 11  # ~11 & 0xf == 0x4
        elif char in '0123456789':
            res = int(char)
        else:
            res = int(char, 16)
        org |= (res << (4 * (15 - i)))
    return org

menu_str = "1_c_3_c_0__ff_3e"
org = reverse_to_org(menu_str)
print(f"Recovered org (hex): {hex(org)}")
print(f"Recovered org (decimal): {org}")