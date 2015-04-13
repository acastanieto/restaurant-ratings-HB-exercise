# your code goes here

# 1.  open file,
# create dictionary
# 2.  for loop: strip, split by ":" into list
# 4.  list[0] aassign to dictionary key with list[1] as value
# 5.  add the key/value pair to the dictionary
# 6.  loop through sorted(dictionary) and print key, value pairs

def parse_scores_file(filename):
    scores = open(filename)
    ratings_dict = {}
    for line in scores:
        restaurant_rating = line.rstrip().split(":")
        ratings_dict[restaurant_rating[0]] = restaurant_rating[1]
    return ratings_dict

def sort_and_print_ratings(ratings_dict):
    for key in sorted(ratings_dict):
        print "Restaurant '%s' is rated %d." % (key, int(ratings_dict[key]))


sort_and_print_ratings(parse_scores_file("scores.txt"))