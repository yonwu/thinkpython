def eval_loop():
    while True:
        a = input("Enter something >>> ")
        if a == "done":
            break
        print(eval(a))

    return eval(a)


if __name__ == "__main__":
    eval_loop()
