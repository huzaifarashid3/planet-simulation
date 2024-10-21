SUN = 100 
BASE_WATER = 100
POPULATION = 100
RAIN = 50

# we provide simulation
# participants try to sustain it 

cloud = 0.5 # controllable # <------------
greenhouse = 0.3 # heat control

rain = 0.4

population = POPULATION 

pollution = 0.2*population

light = (1/cloud) * SUN 
light -= 0.3*pollution*light

evaporation = 0.1 * light 


water = BASE_WATER 
water -= evaporation*water

rain += 0.1*evaporation*water

if rain > 0.8:
    water += 0.7*RAIN
    rain = 0.3


air_quality = 0.1*pollution

plant = 0.6*light + 0.3*water + 0.1*air_quality
animal = 0.3*plant + 0.7*water

population += 0.5*animal + 0.3*plant + 0.2*water
population -= 100 # dying rate

air_quality += 0.2*plant

water -= 0.2*population +  0.2*plant + 0.2*animal

# handle plant and population death


# NOTES
# a balanced water cycle

def foo():
    pass

def myfoo(time):
    return sin(time)


time = 0
for days in range(100):
    # cloud = input() # slider
    cloud = myfoo(time, population, rain) 

    population = foo(cloud, time)
    plant = foo(cloud, population, time)
    print(population)
    print(plant)
    score = 0.2*population - 0.1*pollution
    print(score)