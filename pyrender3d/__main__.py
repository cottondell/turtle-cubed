if __name__ == '__main__':
    print("Demo mode")
    print("1 - Rotating cube")
    print("2 - Controllable cube")
    demo = int(input("Which demo do you want to run: "))

    if demo == 1:
        from .demos import rotating_cube
    elif demo == 2:
        from .demos import controllable_cube
    else:
        print("Invalid demo! Exiting...")
