# Your code here
import re


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    for path in files:
        path.split("/")
        print(path)
    print(files)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
