from TCGA_matchmaker import match_computation as m

def test_compute_dist_gen():
	profile = 2
	sample_data = 3
	expected_distance = 2
	distance = m.compute_distance(profile, sample_data)
	assert distance == expected_distance, "The distance between 2 and 3 is " + str(expected_distance) + " not " + str(distance)

