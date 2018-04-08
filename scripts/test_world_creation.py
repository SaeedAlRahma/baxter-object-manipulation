from klampt import *
import sys
import time
from klampt.sim import *
from klampt import vis

if __name__ == "__main__":
    if len(sys.argv)<=1:
        print "USAGE: visualize_world.py [world_file]"
        exit()
    world = WorldModel()
    for fn in sys.argv[1:]:
        res = world.readFile(fn)
        if not res:
            raise RuntimeError("Unable to load model "+fn)


    vis.add("world",world)
    vis.show()

    t0 = time.time()
    while vis.shown():
        t1 = time.time()
	#update your code here
       	time.sleep(max(0.01-(t1-t0),0.001))
       	t0 = t1
