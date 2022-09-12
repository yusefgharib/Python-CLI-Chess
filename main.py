from Board import Board

def main():
    b = Board(8)
    for row in b.display():
        print(row)

if __name__ == "__main__":
    main()