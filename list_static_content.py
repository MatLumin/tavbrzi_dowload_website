from typing import * 
import os 

def do_it()->List[str]:
	return os.listdir("./static")


if __name__ == "__main__":
	# tetsing 
	print(do_it())