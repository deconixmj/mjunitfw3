"python selenium unittest page object model,testcases" 
Parallel execution using multiprocessing module.

from multiprocessing import Pool
from testclasses import testmethods
...

tc1="load tc1"
tc2="load tc2"
tc3="load tc3"

test_runner=HtmlTestRunner.HTMLTestRunner(output='reports_dir')

def run():
    p=Pool(processes=3)
    p.map(runner,[tc1,tc2,tc3])

def runner(tc):
    test_runner.run(tc)

if __name__ == '__main__':
    exit(run())
