
def determine_color(s):
    
    x=ord(s[0])-ord('a')+1
    y=int(s[1])
    if (x+y)%2==0:
        return "Black"
    else: 
        return "White"

def main():
    print("Input format: a6, b4, f7, h8")
    s = input().strip()
    if ord(s[0]) in range(ord('a'), ord('h')+1) or ord(s[0]) in range(ord('A'), ord('H')+1) and int(s[1]) in range(1, 9):
        result = determine_color(s)
        print(result)
    else:
        print("error")

if __name__ == "__main__":
    main()