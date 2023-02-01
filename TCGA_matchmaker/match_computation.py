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

def test_match(profile, sample_data, threshold):
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
	distance = 0
	# compute distance here
	return distance