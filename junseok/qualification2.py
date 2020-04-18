def printAnswer(testcase, answer):
	print("Case #{}: {}".format(testcase, answer))


def makeSimpleparentheses(n):
	return "{}{}{}".format('('*n, n, ')'*n)

def removeParentheses(s):
	return s.replace(')(', '')

if __name__ == "__main__":
	totalCase = int(input())

	for testcase in range(totalCase):
		str = input()

		strArr = [ str[i] for i in range(len(str)) ]

		ret = "".join( [makeSimpleparentheses(int(item)) for item in strArr] )

		while ret.find(')(') != -1:
			ret = removeParentheses(ret)

		printAnswer(testcase + 1, ret)

