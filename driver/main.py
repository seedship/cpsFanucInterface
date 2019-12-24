import argparse

def main():
	parser = argparse.ArgumentParser(description='TUM Chair of Cyber Physical Systems in Production Engineering FANUC Robot Driver')
	parser.add_argument('--robot_http_endpoint', required=True, type=str, help='http endpoint of the robot')
	args = parser.parse_args()

if __name__ == "__main__":
	main()
