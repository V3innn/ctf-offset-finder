# CTF Offset Finder

CTF Offset Finder is a Python script that utilizes pwntools to find the offset for CTF challenges in 32-bit binaries. It helps determine the precise location within a buffer where the program's execution flow can be controlled or redirected.

## Features

- Automatically calculates the offset for a target function in a 32-bit binary.
- Uses a cyclic pattern to trigger crashes and determine the offset.
- Supports both local and remote binary execution.

## Requirements

- Python 3.6 or above
- pwntools library (`pip install pwntools`)

## Usage

1. Clone the repository:

```shell
git clone https://github.com/Leasss/ctf-offset-finder.git
```

2. Navigate to the project directory:

```shell
cd ctf-offset-finder
```

3. Modify the script offset_finder.py to specify the path to your target      binary and the name of the vulnerable function.

4. Run the script:
```shell
python offset_finder.py
```

The offset for the target function will be printed to the console.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
