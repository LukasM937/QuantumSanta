"""This file is used to store and menage the tests for the script"""


def test_all_give_someone(part_list):
    """Test if all particepants sends to someone"""
    for p in part_list:
        if p.receiver is None:
            return False
    return True


# TODO: Test if all particepants recieve from someone.


def test_no_self_loops(part_list):
    """Test if self loops are present.
    Self loops meen that one particepant draw him/her/them -self"""
    for p in part_list:
        if p.id == p.receiver.id:
            return False
    return True


def test_no_second_order_loops(part_list):
    """Test if the cardinality of a smallest loop is larger than two
    - optional criteria"""
    for p in part_list:
        if p.receiver is not None:
            if p.receiver.receiver is not None:
                if p.id == p.receiver.receiver.id:
                    return False
    return True


def test_other_num_still_pressent(number, part_list, output_array):
    """Test if the remainding particepants IDs are still preasent in the randome array.
    This is an indication for a deadlock."""
    for i in range(len(part_list)):
        if (i is not number) and (i in output_array):
            return True
    return False
