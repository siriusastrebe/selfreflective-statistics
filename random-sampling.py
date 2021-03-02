# 
#
#```
#If you chose an answer to this question at random, what is the probability you will be correct?
#(a) 25%
#(b) 50%
#(c) 50%
#(d) 100%
#```

import random 

iterations = 100000
options = [.25, .5, .5, 1]
samples = {
  .25: 0,
  .5: 0,
  1: 0
}

for i in range(0, iterations):
  index = random.randint(0, 3)
  sample = options[index]
  # Round so we avoid rounding-issues for floating point numbers
  samples[round(sample, 2)] += 1

for key, total in samples.items():
  if (abs((total/iterations) - float(key)) < 0.01):
    print("%s is close to correct at %f" % (str(round(key, 2)), (total / iterations)))
