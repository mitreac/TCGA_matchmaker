from TCGA_matchmaker import match_computation as m
import pandas as pd 

def test_hello():
	expected_result = "Hello, there, BIOINF 576!"
	computed_result = m.hello_there("BIOINF 576")
	print(computed_result)
	assert expected_result == computed_result, "The expected result does not match the computed one"


def test_compute_dist_gen():
	profile = pd.Series([2,3,4], index = ["g1","g2","g3"])
	sample_data = pd.Series([2,4,4,5], index = ["g1","g2","g4","g5"])
	expected_distance = 1
	distance = m.compute_distance(profile, sample_data)
	assert distance == expected_distance, "The distance between " + \
		str(profile) + " and " + \
		str(sample_data) + " is " + \
		str(expected_distance) + " not " + str(distance)



def test_compute_match_scores_gen():
	profile = pd.Series([2,3,4], index = ["g1","g2","g3"])
	samples_data = pd.DataFrame([[2,2,2], [4,4,5], [4,5,5], [5,5,5]], 
								index = ["g1","g2","g4","g5"], 
								columns = ["s1","s2","s3"])
	expected_scores = pd.Series([1,1,2], index = ["s1","s2","s3"])
	scores = m.compute_match_scores(samples_data, profile)
	assert sum(scores == expected_scores) == len(scores), \
							"The match scores between " + str(profile) + \
							" and " + str(samples_data) + " is " + \
							str(expected_scores) + " not " + str(scores)
