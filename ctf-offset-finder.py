from pwn import *

def banner():
    print("                                     .-')      ('-.   .-') _                                .-') _  _ .-') _     ('-.     ('-.  _  .-')   ")
    print("                                    ( OO ).  _(  OO) (  OO) )                              ( OO ) )( (  OO) )  _(  OO)  _(  OO)( \( -O )  ")
    print(" .-'),-----.    ,------.   ,------.(_)---\_)(,------./     '._          ,------.,-.-') ,--./ ,--,'  \     .'_ (,------.(,------.,------.  ")
    print("( OO'  .-.  '('-| _.---'('-| _.---'/    _ |  |  .---'|'--...__)      ('-| _.---'|  |OO)|   \ |  |\  ,`'--..._) |  .---' |  .---'|   /`. ' ")
    print("/   |  | |  |(OO|(_\    (OO|(_\    \  :` `.  |  |    '--.  .--'      (OO|(_\    |  |  \|    \|  | ) |  |  \  ' |  |     |  |    |  /  | | ")
    print("\_) |  |\|  |/  |  '--. /  |  '--.  '..`''.)(|  '--.    |  |         /  |  '--. |  |(_/|  .     |/  |  |   ' |(|  '--. (|  '--. |  |_.' | ")
    print("  \ |  | |  |\_)|  .--' \_)|  .--' .-._)   \ |  .--'    |  |         \_)|  .--',|  |_.'|  |\    |   |  |   / : |  .--'  |  .--' |  .  '.' ")
    print("   `'  '-'  '  \|  |_)    \|  |_)  \       / |  `---.   |  |           \|  |_)(_|  |   |  | \   |   |  '--'  / |  `---. |  `---.|  |\  \  ")
    print("     `-----'    `--'       `--'     `-----'  `------'   `--'            `--'    `--'   `--'  `--'   `-------'  `------' `------'`--' '--' ")


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

def main():
    banner()
    binary_path = input("Enter the path to the binary: ").strip()
    target_func = input("Enter the target function name: ").strip()
    find_offset(binary_path, target_func)

if __name__ == "__main__":
    main()
