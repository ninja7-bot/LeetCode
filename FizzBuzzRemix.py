import sys

def FizzBuzzRemix(n):
    count = 0
    for i in range(n + 1):  # Fixing range to include 'n'
        if i % 3 == i % 5:
            count += 1
    return count


def main():
    t = int(sys.stdin.readline().strip())
    results = []
    
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        results.append(str(FizzBuzzRemix(n)))
    
    print("\n".join(results))  

if __name__ == "__main__":
    main()
