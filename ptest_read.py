'''
python profile : read this
python -m cProfile -o output.txt ptest.py
'''

import pstats
p = pstats.Stats("output.txt")
p.strip_dirs().sort_stats(-1).print_stats()