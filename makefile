FILES :=                              \
    .travis.yml                       \
    netflix-tests/tu564-RunNetflix.in   \
    netflix-tests/tu564-RunNetflix.out  \
    netflix-tests/tu564-TestNetflix.py  \
    netflix-tests/tu564-TestNetflix.out \
    Netflix.html                      \
    Netflix.log                       \
    Netflix.py                        \
    RunNetflix.py                     \
    RunNetflix.in                     \
    RunNetflix.out                    \
    TestNetflix.py                    \
    TestNetflix.out

all:

check:
	@for i in $(FILES);                                         \
    do                                                          \
        [ -e $$i ] && echo "$$i found" || echo "$$i NOT FOUND"; \
    done

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  Netflix.html
	rm -f  Netflix.log
	rm -f  RunNetflix.out
	rm -f  TestNetflix.out
	rm -rf __pycache__

config:
	git config -l

test: RunNetflix.out TestNetflix.out

Netflix-tests:
	git clone https://github.com/cs373-summer-2015/netflix-tests.git

Netflix.html: Netflix.py
	pydoc3 -w Netflix

Netflix.log:
	git log > Netflix.log

RunNetflix.out: RunNetflix.py
	cat RunNetflix.in
	./RunNetflix.py < RunNetflix.in > RunNetflix.out
	cat RunNetflix.out

run:
	RunNetflix.py < RunNetflix.in

probe:
	RunNetflix.py < probe.txt

time1:
	time RunNetflix.py < RunNetflix.in

time2:
	time RunNetflix.py < probe.txt > probe.out

TestNetflix.out: TestNetflix.py
	coverage3 run    --branch TestNetflix.py >  TestNetflix.out 2>&1
	coverage3 report --omit=/v/filer4b/v38q001/tumrod/.local/lib/python3.4/site-packages/numpy/* -m >> TestNetflix.out
	cat TestNetflix.out

