from madlibs_programs import animal, bird, human
import random

if __name__ == "__main__":

    animal.madlib()

    animal.madlib2()
     
    m = animal
    m.madlib()

    m = random.choice([animal, bird, human])
    m.madlib()
