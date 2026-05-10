# Section 1.1
def get_topics(questions):
	return {
		topic
		for q in questions
		for topic in q[1]
	}
def get_total_time(questions):
	return sum([q[2] for q in questions])

# Section 1.2
1, 4, 7, 301

# Section 1.3
def design_exam(questions, duration):
	all_topics = get_topics(questions)
	def helper(topics, questions, duration):
		if duration < 0:
			return None
		if not topics:
			return set()
		if not questions:
			return None
		temp = helper(topics - questions[0][1], questions[1:], duration-questions[0][2])
		if temp is not None:
			return {questions[0][0]} | temp
		return helper(topics,questions[1:], duration)
	return helper(all_topics, questions, duration)

# Section 2
def gen_slice(iterable, start, stop, step):
	idx = 0
	for e in iterable:
		if idx%step == start%step and start <= idx and idx < stop:
			yield e
		idx += 1

# Section 3: on paper

# Section 4:
def potluck(people):
	people_list = list(people.keys())
	def helper(foods_so_far, remaining_people):
		# base case
		if not remaining_people:
			return [{}]
		# recursive case
		answer = []
		first_person = remaining_people[0]
		for food in people[first_person] if food not in foods_so_far:
			for temp_dict in helper(foods_so_far | {food}, remaining_people[1:])
				temp_dict[food] = first_person
				answer.append(temp_dict)
		return answer
	return helper(set(), people_list)

# Section 5.1:
def length(L):
	counter = 0
	sublist = L
	while not sublist==[None]:
		sublist = sublist[1]
		counter += 1
	return counter
def delete(L, index):
	if index < 0 or index >= length(L):
		raise IndexError
	def rev_delete(L, revindex):
		if revindex==0:
			return L[1]
		return [L[0], rev_delete(L[1], revindex-1)]
	return rev_delete(L, length(L)-1-index)

# Section 6.1
"""
[True, False, False, True, True]
[True, True, True, True, True]
[False, False, False, False, False]
"""
def mystery1a(func, inp):
	return [func(e) for e in inp]

# Section 6.2
"""
True
True
False
"""
def mystery2a(func, inp):
	return any([func(e) for e in inp])

# Section 7
"""
line 23 -- only converts the array to a tuple of rows, but each row is still a list; the resulting behavior is that board[i] is a mutable list for each row i, so calling find_path fails
line 34 -- does not check for boundaries; the resulting behavior is that when someone tries to toggle a boundary, an IndexError gets raised
line 35 -- does not save the result of calling flip_single_light; the resulting behavior is that "out" does not get modified
"""
