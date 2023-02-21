from lucky_number_Richard_Fehling import shorter_lucky_list

# Test of shorter list function
def test_shorter_lucky_list():
    '''
    Boundaries:
    lucky_list, lucky_number, num_of_attempts and player_input are validated through other functions
    will +/- 30 from lucky_number work as planned
    What if:
    All numbers in lucky_list is within +/- 30 of lucky_number?
    player_input is within the +/- 30 from lucky_number on the first attempt
    will it still be in lucky_list?
    All other numbers than lucky_number are smaller or bigger than +/- 30?
    Also testing added feature of removing first player_input if wrong but still within +/- 30
    '''
    ###########################################################
    # All numbers within and including +/- 30 from lucky_number
    # Testdata
    lucky_list_testdata = [20, 25, 30, 40, 50, 60, 70, 75, 79, 80]
    result = shorter_lucky_list(lucky_list_testdata, 
            lucky_number=50, num_of_attempts=1, player_input=40)
    assert len(result) == 10
    # Will player_input (40) still be in the list?
    assert not 40 in result 
    
    ###########################################################
    # Second attempt, player_input will be removed
    lucky_list_testdata = [20, 21, 30, 40, 50, 60, 70, 75, 79, 80]
    result = shorter_lucky_list(lucky_list_testdata, lucky_number=50, num_of_attempts=2, player_input=40)
    assert len(result) == 9
    # Will player_input (40) still be in the list?
    assert not 40 in result

    ###########################################################
    # All other numbers than lucky_number and player_input 
    # are smaller or bigger than +/- 30?
    # Testdata
    lucky_list_testdata = [ 1, 10, 15, 19, 50,
    79, 81, 90, 95, 100]
    result = shorter_lucky_list(lucky_list_testdata, lucky_number=50, num_of_attempts=1, player_input=79)
    assert len(result) == 1
    assert not 79 in result


def test_2():
        assert 2==2, "Kollar 2"
class Wow:
        def test_3():
                assert 5 >0
    



