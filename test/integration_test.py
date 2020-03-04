import driver.fanucfrontend as ffe
import logging
import sys


# A collection of stand alone tests to verify robot behavior

def sandbox():
    frontend = ffe.FANUCFrontEnd("http://10.162.12.191")
    frontend.reset()
    status = frontend.get_status()
    print(status)
    response = frontend.start_motion()
    print("Success?:", response)
    response = frontend.send_motion_request(1500, 0, 100, 0, 0, 0, "lca")
    print("Success?:", response)
    response = frontend.send_motion_request(1300, 0, 200, 0, 0, 0, "lca")
    print("Success?:", response)
    response = frontend.send_motion_request(1700, 0, 200, 0, 0, 0, "lca")
    print("Success?:", response)
    response = frontend.send_motion_request(1500, 0, 100, 0, 0, 0, "lca")
    print("Success?:", response)
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
