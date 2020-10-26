# EXERCISE 1
from numpy.random import rand
from math import sqrt

def estimate_pi_with_monte_carlo(n=1000):
    inside_points = 0
    for _ in range(n):
        x = rand()
        y = rand()
        distance = sqrt(x**2 + y**2)
        if distance < 1:
            inside_points += 1
    return 4 * (inside_points / n)

# estimate of PI with 1000 points
print('Pi estimate:', estimate_pi_with_monte_carlo())


#EXERCISE 2
from numpy.random import rand
# parabolas
p1 = lambda x: x**3
p2 = lambda x: 2*x - x**2

# upperbound is 1, lowerbound is 0
def estimate_area_bounded_by_p1_and_p2(n=10000,l=0,u=1):
    p1_sum = 0
    p2_sum = 0
    for _ in range(n):
        x = rand()
        p1_sum += p1(x)
        p2_sum += p2(x)
    p1_area = ((u - l)/n) * p1_sum
    p2_area = ((u - l)/n) * p2_sum
    return p2_area - p1_area

print(estimate_area_bounded_by_p1_and_p2())

#HIT AND MISS
def estimate_area_bounded_by_p1_and_p2_using_proportion(n=10000):
    inside_points = 0
    for _ in range(n):
        x = rand()
        y = rand()
        y_p1 = p1(x)
        y_p2 = p2(x)
        if y > y_p1 and y < y_p2:
            inside_points += 1
    return inside_points / n

print(estimate_area_bounded_by_p1_and_p2_using_proportion())

# Efficiency
# Both monte carlo algorithm run on O(n) where n is the number 
# of random data points, first approcah needs extra computation
# but proportion method may slow down depending on the rand function
# Overall, the proportion method is faster if we will not consider
# the random number generation function


#EXERCISE 3
from numpy.random import uniform

def estimate_volume_of_ellipsoid(n=10000):
    box_volume = 14*4*10
    ellipsoid = lambda x,y,z: x**2/49 + y**2/4 + z**2/25
    count = 0
    for _ in range(n):
        x = uniform(-7, 7, 1)
        y = uniform(-2, 2, 1)
        z = uniform(-5, 5, 1)

        if ellipsoid(x,y,z) <= 1:
            count += 1
    return box_volume * (count/n)

print(estimate_volume_of_ellipsoid())


