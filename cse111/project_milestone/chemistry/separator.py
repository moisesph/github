"""Separate many items and put them to put them in my code """

def main():
    your_list = input("Enter your list ")
    separator_by_comas(your_list)

def separator_by_comas(your_list):
    separated = your_list.split()
    return separated

if __name__ == "__main__":
    main()