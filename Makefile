.PHONY: test problem_1 problem_2

# Run All Tests
test: problem_1 \
	  problem_2 \
	  problem_29 \
	  problem_41 \
	  problem_70 \
	  problem_83

problem_1:
	${INFO} "Test Problem 1"
	@ (cd src/tests ; python problem_1_tests.py -v)
	${INFO} "Complete!"

problem_2:
	${INFO} "Test Problem 2"
	@ (cd src/tests ; python problem_2_tests.py -v)
	${INFO} "Complete!"

problem_29:
	${INFO} "Test Problem 29"
	@ (cd src/tests ; python problem_29_tests.py -v)
	${INFO} "Complete!"

problem_41:
	${INFO} "Test Problem 41"
	@ (cd src/tests ; python problem_41_tests.py -v)
	${INFO} "Complete!"

problem_70:
	${INFO} "Test Problem 70"
	@ (cd src/tests ; python problem_70_tests.py -v)
	${INFO} "Complete!"

problem_83:
	${INFO} "Test Problem 83"
	@ (cd src/tests ; python problem_83_tests.py -v)
	${INFO} "Complete!"

# Output Formatting
CYAN := "\e[1;36m"
NC := "\e[0m"
INFO := @bash -c '\
    printf $(CYAN); \
    echo "=> $$1"; \
    printf $(NC)' VALUE
