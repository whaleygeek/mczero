# minecraft.py  (c) 2017 D.J.Whale  15/01/2017
#
# Based on ideas by D.J.Whale on 10/06/2016 (see ideas.txt)

# usage:
#   from minecraft import * (bit like from turtle import *)
#   import minecraft (bit like import turtle)

# TODO: Needs to be a class with module wrappers,
# so that like turtle, we could have a default single minecraft,
# or multiple minecrafts

# TODO: Items that are player centric, need to support multi-instances players
# where the underlying world is multi player.
# This also implies methods to get a player identity from their name,
# list player names, get number of players, etc.

# TODO: Not sure, could add when_xxx event handlers for certain events
# such as:
#  'when this block is hit'
#  'when a player joins the game'
#  'when a player leaves the game'
#  'when this block is changed' (might be slow, implies block polling)
#  'when player standing on this block pos' (not as slow, can track player pos)

##import mcpi.minecraft as ll_minecraft # low level minecraft

# the actual connection to the Minecraft world
world     = None

# the server address to connect to, user can override
server    = None

# Will be based on code I posted to the 'Adventures in Minecraft' forum
direction = None # direction estimator based on real movement

# A stack of positions we have teleported from, so we can teleport_back()
teleport_stack = []



def auto_create(m): # DECORATOR for any method
    """Auto create if not already created"""
    def wrapped(*args, **kwargs):
        global world
        if world is None:
            if server is None:
                world = create()
            else:
                world = create(server)
        return m(*args, **kwargs)

    return wrapped


#----- CONNECTION

def create(addr=None):
    """Create a connection to a server"""
    pass


#----- CHAT

@auto_create
def chat(msg):
    """Send a message to the chat"""
    pass


#----- PLAYER POSITION

# TODO: decide if using relative or absolute coordinate system.
#   might be nice to be switchable.
#   def relative() - all relative to player.getTilePos()
#   def absolute() - all absolute positions
#   but take care if you get a position of something physical
#   you might want that to be absolute
#   so some methods might always be absolute
#   and some might always be relative
#   and some might be switchable.
#   might want a naming convention for coordinates
#   rel if always relative
#   abs if always absolute
#   no prefix if could be switchable between either system

# could have a separate module for coordinate maths
# to do things like distance_between()
# as it's not really part of the core api
# but a set of maths library helpers.
# coordinates could be an object but work like tuples/variables
# to allow this to be added later. Not sure.
# teleport(here()+random.randint(10)) # radius of 10 around here?

##def relative():
##    pass

##def absolute():
##    pass

@auto_create
def here(): # -> (x,y,z)
    """Work out where the player is standing"""
    pass

@auto_create
def facing(direction=None):
    """Work out which direction our direction estimator thinks we are facing"""
    #facing()->direction or None
    #facing(direction)->bool
    pass

@auto_create
def moving(dirn=None):
    """What direction am I moving, or am I moving in a direction"""
    # NORTH, EAST, SOUTH, WEST
    # if moving(dirn)
    # dirn = moving()
    pass

@auto_create
def moved():
    """Have we moved since we last checked?"""
    pass # true if moved since last check

@auto_create
def move_by(*args):
    """Move player by a specific distance"""
    #NOTE: some choices to make here about 'facing direction'
    #see my direction estimator, might use that here.
    # xd,yd=None,zd=None
    # tuple(xd,yd,zd)
    pass

@auto_create
def jump(height=None):
    """Jump up into the sky"""
    #height=None (player.y+5)
    #height=n (player.y+n)
    pass

@auto_create
def north(amount):
    """move north by a distance"""
    pass

@auto_create
def east(amount):
    """move east by a distance"""
    pass

@auto_create
def south(amount):
    """move south by a distance"""
    pass

@auto_create
def west(amount):
    """move west by a distance"""
    pass

@auto_create
def forward(amount=1):
    """Move forward based on direction estimator"""
    pass

@auto_create
def backward(amount=1):
    """Move backward based on direction estimator"""
    pass

@auto_create
def left(amount=1):
    """Move left based on direction estimator"""
    pass

@auto_create
def right(amount=1):
    """Move right based on direction estimator"""
    pass

def up(amount=1):
    """Set above me to air, and move up by one"""
    pass

def down(amount=1):
    """Set below me to air, and move down by one"""
    pass

@auto_create
def turn_right():
    # affects facing direction, might not turn graphic
    pass

@auto_create
def turn_left():
    """Turn right based on direction estimator"""
    # affects facing direction, might not turn graphic
    pass

@auto_create
def teleport_to(*args):
    """Move player to a new location"""
    # x,y,z
    # tuple(x,y,z)
    # push current position onto a teleport stack
    pass

def teleport_back():
    """Move player to previous teleport position"""
    # pop from teleport stack, if not None, teleport there
    # if stack empty, just display a warning?
    pass


#----- BLOCK CREATION

@auto_create
def drop(block):
    """Drop a block under your feet"""
    # blockid
    # string name
    # builds at current player position under feet
    pass

@auto_create
def build(block, *args):
    """Build one or more blocks"""
    #TODO:  decide if relative or absolute
    # block_id_or_str
    # block_id_or_str, extradata_id_or_str
    # e.g. names of extradata associated with block type
    # and validated, "wool", "red" but not "planks", "red"
    # b, x, y, z
    # b, (x, y, z)
    # b, x1, y1, z1, x2, y2, z2
    # b, (x1, y1, z2), (x2, y2, z2)
    pass

#----- BLOCK SENSING

@auto_create
def standing_on(b=None):
    """What are we standing on, or are we standing on a specific block?"""
    # if b not None, bool result if standing on b
    # if b none, return blockid of what standing on
    # blockid is an object that when inspected, prints string name
    pass

@auto_create
def height(*args):
    """What is the world height at a position"""
    # height() at current pos
    # height(x, z) at this pos
    # height(x, y, z) at this pos
    # height((x,y,z)) at this pos
    pass

@auto_create
def was_hit(*args):
    """Was this block/face hit?"""
    # was_hit(x,y,z)
    # was_hit(x,y,z,face)
    # was_hit((x,y,z))
    # was_hit((x,y,z),face)
    pass

@auto_create
def get_hit():
    """Get the last hit pos and face"""
    pass


#----- HELP

def help(topic=None):
    # help()
    # help(standing_on)
    # help("blocks")
    print("Sorry, no help yet")


#---- IDEAS
# other (random) ideas
#   load(file, coords, size)     - loads CSV3D file into coords
#   save(coords, size, file)     - saves coords region into CSV3D file
#   photo(file)                  - take a screenshot of minecraft window and store it in a file
#   build(object)                - using minecraftstuff alias object.build
#   move(object)                 - using minecraftstuff alias object.move
#   rotate(object)               - using minecraftstuff alias object.rotate
#   load(file, object)[->object] - load object defn from file into minecraftstuff object alias object.load
#   save(object, file)           - save minecraftstuff object to a file alias object.save

# north()
# house = load("house")
# build(house, here())
# south(-10)
# photo("my_house.png")

# END



