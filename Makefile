.PHONY: test problem_1 problem_2

# Run All Tests
test: problem_1 \
	  problem_2

problem_1:
	${INFO} "Test Problem 1"
	@ (cd src/tests ; python problem_1_tests.py -v)
	${INFO} "Complete!"

problem_2:
	${INFO} "Test Problem 2"
	@ (cd src/tests ; python problem_2_tests.py -v)
	${INFO} "Complete!"

# Output Formatting
CYAN := "\e[1;36m"
NC := "\e[0m"
INFO := @bash -c '\
    printf $(CYAN); \
    echo "=> $$1"; \
    printf $(NC)' VALUE
