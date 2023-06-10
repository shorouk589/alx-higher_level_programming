#!/usr/bin/python3

if __name__ == "__main__":
    """Prints alll namess definned by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
