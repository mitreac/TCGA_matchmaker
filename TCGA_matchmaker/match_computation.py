import numpy as np
import pandas as pd

def read_expr_profile(file_name):
	# implemented
	profile_data = pd.read_csv(file_name, sep = "\t")
	return profile_data

def read_TCGA_sample(file_name):
	# implemented
	sample_data = None
	# read sample data
	return sample_data

def check_match(profile, sample_data, threshold):
	is_match = False
	is_present = check_profile(profile, sample_data)
	if is_present:
		distance = compute_distance(profile, sample_data)
		is_match = distance < threshold
	return is_match

def check_profile(profile, sample_data):
	is_present = False
	# check if all genes in the profile are present
	return is_present

def compute_distance(profile, sample_data):
	"""
	Compute the distance between the reference expression profile 
	and a sample expression profile

	Parameters:
		profile (pandas.Series): a pandas series with the reference profile
								data is the expression level, 
								rownames are gene symbols or IDs
		sample_data(pandas.Series): a pandas series with the sample profile
								data is the expression level, 
								rownames are gene symbols or IDs

	Returns (float): match score - a distance type metric that shows how close the profiles are
									0 would be minimum and 1 would be maximum 

	"""
	distance = 0
	# compute distance here
	set1 = set(sample_data.index)
	set2 = set(profile.index)
	intersection = set1.intersection(set2)
	overlap_no = len(intersection)
	smaller_set_no = min(len(set1), len(set2))
	perc_overlap = overlap_no/smaller_set_no
	if (perc_overlap > 0.6):
		distance = sum(abs(sample_data[intersection] - profile[intersection]))
	return distance
