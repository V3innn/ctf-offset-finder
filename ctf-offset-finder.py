from pwn import *

def find_offset(binary_path, target_func):

    p = process(binary_path)

    cyclic_pattern = cyclic(2000)
    payload = cyclic_pattern
    p.sendline(payload)
    p.wait()
    # For 32-bit binaries use "eip", for 64-bit binaries use "rip"
    crashed_eip = p.corefile.eip 

    # Use n=8 for 64-bit binaries
    offset = cyclic_find(crashed_eip, n=4)

    print(f"The offset for '{target_func}' in '{binary_path}' is: {offset}")

    p.close()

# Usage example
# Assuming 'vuln' is in the current directory, if not write the fullpath
binary_path = './vuln' # The name of the binary
target_func = 'win' # The function that we want to target
find_offset(binary_path, target_func)
