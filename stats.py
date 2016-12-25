"""This code reads grades of students from a file and calculates:
the measures of central tendency (mean, median) and measures of dispersion (variance, standard deviation, interquartile range)
and z-scores"""

grades = []
#read the file and store all the grades in grades list:
with open("grades.txt", "r") as f:
    for line in f:
        grades.append(float(line.strip()))

def grades_sum(scores):
    total = 0
    for grade in scores: 
        total += grade
    return total
    
def grades_average(scores):
    sum_of_grades = grades_sum(scores)
    average = sum_of_grades / float(len(scores))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance+= (average-score)**2
    variance = variance/float(len(scores))
    return variance


def grades_std_deviation(variance):
    return variance ** 0.5

variance = grades_variance(grades)
std_deviation = grades_std_deviation(variance)
mean= grades_average(grades)

def median(scores):
    sort=sorted(scores)
    if (int(len(sort)) %2) != 0:
        mid= (len(sort)+1) /2
        return sort[mid-1]
    else:
        mid= len(scores) /2
        return (sort[mid-1]+sort[mid])/2.0
    
median_scores = median(grades)

def interquartiles(scores):
    median_scores = median(scores)
    sort=sorted(scores)
    if (int(len(scores)) %2) != 0:
        mid = (len(scores)+1) /2
        first_quartile = sort[(mid - (mid/2))-1]
        third_quartile = sort[(mid + (mid/2))-1]
    else:
        mid= len(scores) /2
        first_quartile = (sort[(mid - (mid/2))-1]+sort[(mid - (mid/2))])/2.0
        third_quartile = (sort[(mid + (mid/2))-1]+sort[(mid + (mid/2))])/2.0
    return [first_quartile, median_scores, third_quartile]
    
def z_score(scores, std_deviation, mean):
    z_scores=[]
    for x in scores:
        z_scores.append((x-mean)/std_deviation)
    return z_scores
z_scores = z_score(grades, std_deviation, mean)

print "Grades: \n %s" % grades
print "sum of grades: %f " % grades_sum(grades)
print "Average grade: %f" % grades_average(grades)
print "Median of grades: %f" % median_scores
print "Interquartiles: %s" % interquartiles(grades)
print "Variance: %f" % variance
print "Standard Deviation: %f" % std_deviation
print "z-scores:\n %s" % zip(grades, z_scores)

