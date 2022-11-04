from project.elf import Elf
from project.hero import Hero
from project.soul_master import SoulMaster

# https://judge.softuni.org/Contests/Compete/Index/1941#2

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
soul_master = SoulMaster("Z", 8)
print(soul_master.__class__)
print(soul_master.__class__.__bases__)