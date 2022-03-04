#need to seperate out because will be best practice moving forward
import addNums as add   # need to reference the file where the function is


def test_addNums_passingTest():
    output = add.addNums(1,2) #call the file and the function here to do the work
    assert output == 3, "should pass"


def test_addNums_notPassingTest():
    output = add.addNums(2,2) #call file and function
    assert output == 6, 'should not pass'
