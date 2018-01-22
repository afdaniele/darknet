# @Author: Andrea F. Daniele <afdaniele>
# @Date:   Sunday, January 21st 2018
# @Email:  afdaniele@ttic.edu
# @Last modified by:   afdaniele
# @Last modified time: Sunday, January 21st 2018


# Stupid python path shit.
# Instead just add darknet.py to somewhere in your python path
# OK actually that might not be a great idea, idk, work in progress
# Use at your own risk. or don't, i don't care

import sys, os
sys.path.append(os.path.join(os.getcwd(),'python/'))

import darknet as dn
import pdb

dn.set_gpu(0)
net = dn.load_net("cfg/yolo.cfg", "yolo.weights", 0)
meta = dn.load_meta("cfg/coco.data")


r = dn.detect(net, meta, "data/eagle.jpg")
print r
