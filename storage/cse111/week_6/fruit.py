def main():
  # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    fruit_list.reverse()
    print(f"reverse: {fruit_list}")

    fruit_list.append("Orange")
    print(f"append: {fruit_list}")


    for fruit in fruit_list:
        if "apple" == fruit:
            fruit_list.insert(-4, "cherry")
            print(f"Inserted: {fruit_list}")
            break
        
    fruit_list.remove("banana")
    print(f"remove: {fruit_list}")

    
    
    removed = fruit_list.pop(3)
    print(f"removed: {removed}")

if __name__ == "__main__":
    main()