# -*- coding: utf-8 -*-
"""

Population Vector Decoding of a Directional Stimulus
Created on Mon Jan 19 15:41:28 2026

"""

# Import necessary libraries
import numpy as np
import pickle

# Open the file containing neural responses to the unknown stimulus
with open('_e96f8f1cf1f8256c8595dcb9668fee4f_pop_coding_3.4.pickle', 'rb') as f:
    pop = pickle.load(f) # Dictionary with r1, r2, r3, r4 and c1, c2, c3, c4

# Open the file containing tuning curves for all neurons
with open('_e96f8f1cf1f8256c8595dcb9668fee4f_tuning_3.4.pickle', 'rb') as f:
    tuning = pickle.load(f)

# Dictionary to store the maximum mean firing rate for each neuron
rmax = {}

for i in range(1, 5):
    # Compute the mean tuning curve across trials
    mean_tuning = np.mean(tuning[f'neuron{i}'], axis=0)
    
    # Store the maximum value of the tuning curve
    rmax[i] = np.max(mean_tuning)

# Initialize x and y components of the population vector
Vx, Vy = 0.0, 0.0

for i in range(1, 5):
    # Mean firing rate of neuron i during the unknown stimulus
    r_mean = np.mean(pop[f'r{i}'])    
    
    # Preferred direction vector of neuron i (unit vector)
    ci = pop[f'c{i}']  
    
    # Normalize the response using the maximum firing rate
    weight = r_mean / rmax[i]
    
    # Add the weighted vector contribution to the population vector
    Vx += weight * ci[0]
    Vy += weight * ci[1]

# Compute the angle in radians
# The convention is: 0° = north (positive y-axis), 90° = east (positive x-axis)
angle_rad = np.arctan2(Vx, Vy)

# Convert from radians to degrees
angle_deg = np.degrees(angle_rad)

# Make sure the angle is in the range [0, 360)
angle_deg = angle_deg % 360

print(round(angle_deg))


