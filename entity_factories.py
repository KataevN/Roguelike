from entity import Entity

player = Entity(char="@", color=(255, 255, 255), name="Player", blocks_movement=True)

rat = Entity(char="r", color=(63, 127, 63), name="Rat", blocks_movement=True)
zombie = Entity(char="Z", color=(0, 127, 0), name="Zombie", blocks_movement=True)