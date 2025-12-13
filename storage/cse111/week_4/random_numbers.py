import random

words = ["XD","LoL", "meme", "Alemaniaa"]

def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    word_list =[]
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 3)
    print(numbers)
    append_random_words(word_list, 4)
    print(words)
    print(word_list)

def append_random_words(w_list, quantity=1):
    for _ in range(quantity):
        w_list.append(random.choice(words))
        


def append_random_numbers(num_list, quantity=1):
    for _ in range(quantity):
        num = random.uniform(1,100)
        num = round(num, 1)
        num_list.append(num)


if __name__ == __name__:
    main()