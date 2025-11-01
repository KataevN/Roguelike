from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor

player = Actor(
    char="@",
    color=(255, 255, 255), 
    name="Player", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
    )

rat = Actor(
    char="r", 
    color=(63, 127, 63), 
    name="Rat", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=5),
    )

zombie = Actor(
    char="Z", 
    color=(0, 127, 0), 
    name="Zombie", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
    )