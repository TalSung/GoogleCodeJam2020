def printAnswer(testcase, trace, dupRow, dupCol):
	print("Case #{}: {} {} {}".format(testcase, trace, dupRow ,dupCol))


if __name__ == "__main__":
	totalCase = int(input())

	for testcase in range(totalCase):
		n = int(input())
		trace = 0
		dRow = 0
		dCol = 0

		colSetList = [ set() for _ in range(n) ]
		for r in range(n):
			rowSet = set()
			row = [int(s) for s in input().split(" ")]

			if n != len(set(row)):
				dRow += 1

			trace += row[r]

			for idx, item in enumerate(row):
				colSetList[idx].add(item)

		for colSet in colSetList:
			if n != len(colSet):
				dCol += 1

		printAnswer(testcase + 1, trace, dRow, dCol)

