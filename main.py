import argparse
import logging
import sys

from io import StringIO
from driver.djangofrontend import DjangoFrontEnd
from driver.fanucfrontend import FANUCFrontEnd

def main():

	# Setup debug logging
	logger = logging.getLogger()
	logger.propagate = False
	logger.level = logging.DEBUG
	stream_handler = logging.StreamHandler(sys.stdout)
	stream_handler.addFilter(lambda r: r.name == "root")
	logger.addHandler(stream_handler)

	# Parse arguments
	parser = argparse.ArgumentParser(description='TUM Chair of Cyber Physical Systems in Production Engineering FANUC Robot Driver')
	parser.add_argument('--robot_endpoint', required=True, type=str, help='http endpoint of the robot')
	parser.add_argument('--django_endpoint', required=True, type=str, help='http endpoint of the django server')
	args = parser.parse_args()

	# Instantiate drivers
	fanucFrontEnd = FANUCFrontEnd(args.robot_endpoint)
	djangoFrontEnd = DjangoFrontEnd(args.django_endpoint)

	# Begin motion
	commands = djangoFrontEnd.make_request()
	fanucFrontEnd.begin_motion()
	for command in commands:
		# Move to command position in absolute cartesian motion with joint interpolation
		fanucFrontEnd.send_motion_request(command['x'], command['y'], command['z'], command['phi'], command['theta'], command['psi'], 'jca')


if __name__ == "__main__":
	main()
