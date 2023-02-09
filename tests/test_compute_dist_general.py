from TCGA_matchmaker import match_computation as m
import pandas as pd 

def test_compute_dist_gen():
	profile = pd.Series([2,3,4], index = ["g1","g2","g3"])
	sample_data = pd.Series([2,4,4,5], index = ["g1","g2","g4","g5"])
	expected_distance = 1
	distance = m.compute_distance(profile, sample_data)
	assert distance == expected_distance, "The distance between " + str(profile) + " and " + str(sample_data) + " is " + str(expected_distance) + " not " + str(distance)

