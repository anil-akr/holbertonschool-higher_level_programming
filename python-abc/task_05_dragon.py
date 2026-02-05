#!/usr/bin/env python3

# Mixins
class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


# Dragon class inherits from both mixins
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")


# Optional test block
if __name__ == "__main__":
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()
