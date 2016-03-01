#!/usr/bin/env python
# This code is under the GPLv2
import os, sys

from hashlib import sha256
from pyew_core import CPyew

class CExpertCluster(object):
	def __init__(self, data):
		self.data = data

	def compareTwoSets(self, set1, set2):
		# Get the ciclomatic complexity statistical data of the 2 samples
		ccs1 = set1.values()[0].program_stats["ccs"]
		ccs2 = set2.values()[0].program_stats["ccs"]

		avg_cc_distance = abs(ccs1["avg"] - ccs2["avg"])
		max_cc_distance = abs(ccs1["max"] - ccs2["max"])
		min_cc_distance = abs(ccs1["min"] - ccs2["min"])
		total_functions = abs(len(set1.values()[0].functions) - len(set2.values()[0].functions))

		difference = avg_cc_distance*0.5 + \
				   max_cc_distance*0.3 + \
				   min_cc_distance*0.1 + \
				   total_functions*0.1
		return difference

	def cluster(self):
		set1 = self.data[0]
		set2 = self.data[1]
		return self.compareTwoSets(set1, set2)

class CGraphCluster(object):
	def __init__(self):
		self.clear()
		self.deep = False
		self.timeout = 0

	def addFile(self, filename):
		self.files.append(filename)

	def clear(self):
		self.files = []
		self.results = []
		self.data = []

	def processFile(self, filename):
		print "[+] Analyzing file %s" % filename
		pyew = CPyew(batch=True)
		pyew.deepcodeanalysis = self.deep
		pyew.analysis_timeout = 0
		pyew.loadFile(filename)

		if pyew.format in ["PE", "ELF"]:
			hash = sha256(pyew.getBuffer()).hexdigest()
			self.data.append({hash:pyew})
		else:
			print "Not a PE/ELF file"

	def compareExpert(self):
		cluster = CExpertCluster(self.data)
		val = cluster.cluster()

		if val == 0:
			print "Expert system: Programs are 100% equals"
		else:
			print "Expert system: Programs differs in %f%s" % (round(val, 1), "%")
		return val

	def processFiles(self):
		for f in self.files:
			self.processFile(f)

def main(prog1, prog2):
	cluster = CGraphCluster()
	cluster.addFile(prog1)
	cluster.addFile(prog2)
	cluster.processFiles()
	cluster.compareExpert()

def usage():
	print "Usage:", sys.argv[0], "file1 file2"

if __name__ == "__main__":
	if len(sys.argv) != 3:
		usage()
	else:
		main(sys.argv[1], sys.argv[2])
