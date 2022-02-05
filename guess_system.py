def answer_check(answer, attempt):
	results = []

	for i, alphabet in enumerate(attempt):
		results.append(compare_strings(alphabet, answer, i))

	return results

def compare_strings(alphabet, answer, index):
	if not exists_and_same_index(alphabet, answer, index):
		for ansAlphabet in answer:
			if not exists_in_word(ansAlphabet, alphabet):
				continue

			return "yellow"

		return "grey"

	return "green"

def exists_and_same_index(alphabet, answer, index):
	if not alphabet == answer[index]:
		return false

	return true

def exists_in_word(ansAlphabet, alphabet):
	if not alphabet == ansAlphabet:
		return false

	return true

if __name__ == "__main__":
	answer = "cocks"
	attempt = "balls"
	print(answer_check(answer, attempt))