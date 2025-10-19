import sys
def even_odd_count(num):
    """
    Return (even_count, odd_count) of the digits in the integer `num`.
    """
    s = str(abs(num))  # ignore sign
    even = sum(1 for ch in s if int(ch) % 2 == 0)
    odd = len(s) - even
    return (even, odd)

if __name__ == "__main__":
    n = int(sys.argv[1])          # read first command-line argument
    print(even_odd_count(n))      # print result