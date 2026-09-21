

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def main():
    labs = sys.argv[1:] or ["lab1", "lab2", "lab3", "lab4"]
    for lab in labs:
        mod = __import__("gen.gen_" + lab, fromlist=["build"])
        print("генерирую %s ..." % lab)
        mod.build()
    print("готово")


if __name__ == "__main__":
    main()
