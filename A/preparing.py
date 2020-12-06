import sys


program_text =  (
"""
#include <iostream>

void checkAfolder() {
    std::cout << "A is OK" << std::endl;
}
"""
)


print("Generating index.h from python3 ...")

target = sys.argv[1]

with open(target, "w") as lib_file:
    lib_file.write(program_text.strip())
