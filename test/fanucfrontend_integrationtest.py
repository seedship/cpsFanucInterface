import driver.fanucfrontend as ffe

# A collection of stand alone tests to verify robot behavior

# Verify robot arm moves
# Verify both joints move
def test_arm_motion():
	frontend = ffe.FANUCFrontEnd("http://10.162.12.191")
	frontend.begin_motion()
	frontend.send_motion_request(0, 0, 0, 0, 90, 0, "jja")
	frontend.send_motion_request(0, 0, 0, 0, 0, 0, "jja")
	frontend.send_motion_request(0, 0, 90, 0, 0, 0, "jja")
	frontend.send_motion_request(0, 0, 0, 0, 0, 0, "jja")
	frontend.stop_motion()

# Verify robot rotates workpiece
def test_rotate():
	frontend = ffe.FANUCFrontEnd("http://10.162.12.191")
	frontend.stop_motion()