#!/usr/bin/env python
import time
from modshogun import Time

parameter_list = [[1],[2]]
def library_time (sleep_secs):
	# measure wall clock time difference
	t=Time()
	time.sleep(sleep_secs)
	diff=t.cur_time_diff()

	# measure CPU time required
	cpu_diff=t.cur_runtime_diff_sec()

	# return results as integers to enable testing
	return round(diff),round(cpu_diff)

if __name__=='__main__':
	print('Time')
	library_time(*parameter_list[0])
