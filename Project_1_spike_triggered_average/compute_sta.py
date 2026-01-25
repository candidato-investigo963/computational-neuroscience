"""
Created on Wed Apr 22 15:21:11 2015

Code to compute spike-triggered average.
"""

# Import necessary libraries
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt



def compute_sta(stim, rho, num_timesteps):
    """
    Compute the spike-triggered average (STA) from a stimulus and spike train.

    Args:
        stim: stimulus time-series (vector of input values over time)
        rho: spike-train time-series (binary vector: 1 if spike, 0 if no spike)
        num_timesteps: how many time steps to include before each spike

    Returns:
        sta: spike-triggered average vector (length = num_timesteps)
    """
        
    # Initialize the STA vector with zeros
    sta = np.zeros((num_timesteps,))

    # Finds the indices of all of the spikes that occur
    # after 300 ms into the recording.
    spike_times = rho[num_timesteps:].nonzero()[0] + num_timesteps
    # .nonzero()[0] returns the indices of all elements that are 1 (spikes)

    # The number of spikes is simply the number of detected spike times.
    # spike_times contains all spike indices after the initial 300 ms,
    # so its length gives the total number of spikes used for the STA.
    num_spikes = len(spike_times)
    print(num_spikes)

    # Compute STA: for each spike, take the previous 'num_timesteps' points in stim
    # and sum them to calculate the average
    
    for spike in spike_times:
        sta += stim[spike - num_timesteps : spike]

    # Divide by the number of spikes to get the average
    sta /= num_spikes

    return sta
    
