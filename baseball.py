import random
from  multiprocessing import Pool


num_threads = 4
num_seasons = 10

avgs = [0] *num_threads

def compute(num_seasons):
    print "Starting thread for num_seasons", num_seasons

    al_east = {"Yankees":0, "Sox":0, "Jays":0, "Rays":0, "Orioles":0}
    avg = {"Yankees":0.0, "Sox":0.0, "Jays":0.0, "Rays":0.0, "Orioles":0.0}

    first_avg = 0.0

    for j in range(num_seasons):
        for i in range(0,162):
            for team in al_east:
                al_east[team] += random.randint(0,1)
        
        first = 0.0
        for team in avg:
            avg[team] += al_east[team]
            if al_east[team] > first:
                first = al_east[team]
            al_east[team] = 0

        first_avg += first

    for team in avg:
        avg[team] = avg[team]/num_seasons

    first_avg /= num_seasons

    return first_avg

pool = Pool(processes = num_threads)

threads = []

print "spinning up threads"
avgs = pool.map(compute, [num_seasons] * num_threads) 

print "joining threads"
pool.close()
pool.join()

first_avg = 0.0
for avg in avgs:
    first_avg += avg

print first_avg/num_threads
