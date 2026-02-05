#!/usr/bin/env python3

# Parent classes
class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


# FlyingFish inherits from both Fish and Bird
class FlyingFish(Fish, Bird):
    def swim(self):
        print("The flying fish is swimming!")

    def fly(self):
        print("The flying fish is soaring!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


# Testing MRO
if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()

    # Print Method Resolution Order
    print(FlyingFish.mro())
    # Or: print(FlyingFish.__mro__)
