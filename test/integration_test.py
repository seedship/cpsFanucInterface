import driver.fanucfrontend as ffe
import logging
import sys
import time


# A collection of stand alone tests to verify robot behavior

def sandbox():
    frontend = ffe.FANUCFrontEnd("http://10.162.12.191")
    frontend.reset()
    status = frontend.get_status()
    print(status)
    response = frontend.start_motion()
    print("Success?:", response)
    response = frontend.send_motion_request(470, 0, -20, 0, 0, 0, "lca")
    print("Success?:", response)
    time.sleep(1)
    response = frontend.send_motion_request(600, 0, 40, 0, 0, 0, "lca")
    print("Success?:", response)
    time.sleep(1)
    response = frontend.send_motion_request(340, 0, 40, 0, 0, 0, "lca")
    print("Success?:", response)
    time.sleep(1)
    response = frontend.send_motion_request(470, 0, -20, 0, 0, 0, "lca")
    print("Success?:", response)
    time.sleep(1)
    response = frontend.stop_motion()
    print("Success?:", response)
    response = frontend.reset()
    print("Success?:", response)


if __name__ == "__main__":
    # Setup debug logging
    logger = logging.getLogger()
    logger.propagate = False
    logger.level = logging.DEBUG
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.addFilter(lambda r: r.name == "root")
    logger.addHandler(stream_handler)

    sandbox()
