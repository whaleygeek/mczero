# minecraft.py  (c) 2017 D.J.Whale  15/01/2017
#
# Based on ideas by D.J.Whale on 10/06/2016 (see ideas.txt)

# usage:
#   from minecraft import * (bit like from turtle import *)
#   import minecraft (bit like import turtle)

def auto_create(m):
    """Auto create if not already created"""
    return m

def create(addr=None):
    pass

@auto_create
def chat(msg):
    pass

@auto_create
def where(): # -> (x,y,z)
    pass

@auto_create
def teleport(*args):
    # x,y,z
    # tuple(x,y,z)
    pass

@auto_create
def moveby(*args):
    # x,y=None,z=None
    # tuple(x,y,z)
    pass

@auto_create
def jump(height=None):
    pass

@auto_create
def north(amount):
    pass

@auto_create
def east(amount):
    pass

@auto_create
def south(amount):
    pass

@auto_create
def west(amount):
    pass

@auto_create
def drop(block):
    # blockid
    # string name
    # builds at current player position under feet
    pass

@auto_create
def build(block, *args):
    # block_id_or_str
    # block_id_or_str, extradata_id_or_str
    # e.g. names of extradata associated with block type
    # and validated, "wool", "red" but not "planks", "red"
    # b, x, y, z
    # b, (x, y, z)
    # b, x1, y1, z1, x2, y2, z2
    # b, (x1, y1, z2), (x2, y2, z2)
    pass

@auto_create
def standing_on(b=None):
    # if b not None, bool result if standing on b
    # if b none, return blockid of what standing on
    # blockid is an object that when inspected, prints string name
    pass

@auto_create
def height(*args):
    # height() at current pos
    # height(x, z) at this pos
    # height(x, y, z) at this pos
    # height((x,y,z)) at this pos
    pass

@auto_create
def was_hit(*args):
    # was_hit(x,y,z)
    # was_hit(x,y,z,face)
    # was_hit((x,y,z))
    # was_hit((x,y,z),face)
    pass

@auto_create
def moved():
    pass # true if moved since last check

@auto_create
def moving(dirn=None):
    # NORTH, EAST, SOUTH, WEST
    # if moving(dirn)
    # dirn = moving()
    pass

def help(topic=None):
    # help()
    # help(standing_on)
    # help("blocks")
    print("Sorry, no help yet")

# END







# END

