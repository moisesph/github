import math

#It needs to read the document still, instead of entering the values
# https://byui-cse.github.io/cse111-ww-course/week02/code-along.html

def main():

    with open("can_list", "r") as file:
        for line in file:
            line.strip()
            name, radius, height, cost = line.split("")
            radius, height, cost = map(int, [radius, height, cost])

    compute_efficiency("#1 picnic", 6.83, 10.16, 0.28)
    compute_efficiency("#1 Tall", 7.78, 10.16, 0.43)
    compute_efficiency(name, radius, height, cost)


def compute_volume(radius, height):
    """
    Computes the volume using radius and height and return it
    """
    volume= math.pi * radius ** 2 * height
    return volume

def compute_area(radius, height):
    area = 2 * math.pi * radius * (radius + height)
    
    return area

def compute_efficiency(name, radius, height, cost):
    area = compute_area(radius, height)
    volume = compute_volume(radius, height)
    efficiency = volume / area
    cost_efficiency = compute_cost_efficiency(volume, cost)
    print(f"{name} volume={volume:.2f} area={area:.2f} efficiency={efficiency:.2f} cost efficiency={cost_efficiency:.2f}%")

def compute_cost_efficiency(volume, cost):
    """
    Computes the cost efficiency of the volume of the steel
    """
    cost_efficiency = volume / cost

    return cost_efficiency

main()