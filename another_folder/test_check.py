
class test_SomeTests():

    def test_3():
        assert 10 == 10



    def test_5():
        num1 = 2
        num2 = 10
        num3 = num1 + 8
        assert num2 == num3

    def test_4():
        print("test 4")
        assert 11==11

def test_outside_class():
        assert 100 > 1

if __name__ == "__main__":
    test = test_SomeTests
    test.test_4()
