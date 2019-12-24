import pytest

import driver.fanucfrontend as ffe

def test_fanucfrontend_init():
	frontend = ffe.FANUCFrontEnd("http://hookbin.com")
	frontend.begin_motion()


def test_fanucfrontend_motion_request():
	frontend = ffe.FANUCFrontEnd("http://hookbin.com")
	frontend.begin_motion()
	frontend.send_request(1,2,3,4,5,6,"jjr")