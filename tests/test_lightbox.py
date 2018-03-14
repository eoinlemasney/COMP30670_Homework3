import lightbox.main2 as ltb
from nose.tools import *

test_url_ok = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt"
test_url_ko = 'http://www.thisdoesnotexist.com/myfile.txt'

test_local_not_formatted = './test_local_not_formatted.txt'
test_local_ok = './test_local.txt'
test_local_ko = './data/nonexisting.txt'


def test_file_read_url():
    f = ltb.read_file(test_url_ok)
    assert len(f) == 2
    assert f[0] != None
    assert f[1] == 1000
    

def test_file_read_local():
    f = ltb.read_file(test_local_ok)
    assert lens(f) == 2
    assert f[0] == 'turn off 660,55 through 986,197\nturn off 341,304 through 638,850'
    assert f[1] == 2


@raises(Exception)
def test_file_read_nonexisting_url():
    ltb.read_file(test_url_ko)

def test_file_read_local():
    f = ltb.read_file(test_local_not_formatted)
    assert len(f) == 2
    assert f[0] == None
    assert f[1] == None