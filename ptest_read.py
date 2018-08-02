'''
python profile : read this
python -m cProfile -o output.txt ptest.py

https://www.blog.pythonlibrary.org/2016/05/24/python-101-an-intro-to-benchmarking-your-code/
http://www.blog.pythonlibrary.org/2014/03/20/python-102-how-to-profile-your-code/
'''

import pstats
p = pstats.Stats("output.txt")
p.strip_dirs().sort_stats(-1).print_stats()