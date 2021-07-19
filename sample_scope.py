def check_scope():
    def do_local():
        test = "local test"

    def non_local():
        nonlocal test
        test = "non local test"

    def do_global():
        global test
        test = "global"

    test = "default"
    do_local()
    print("test value after do_local : " + test)
    non_local()
    print("test value after non do local : " + test)
    do_global()
    print("test value after do_global: " + test)


check_scope()
print(test)
