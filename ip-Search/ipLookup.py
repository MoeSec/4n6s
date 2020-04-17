'''
    File name: ipLookup.py
    Author: Mauricio Tellez Nava
    Email: mtellez91@gmail.com
    Python Version: 3.0
	
	python ipLookup.py input-folder output-file-1.csv output-file-2.csv
	arg1 - the folder that contains files to search
	arg2 - the output filename to store results, breaks down results per file
	arg3 - the output file name to store all results, agregates the results for all files
'''

import sys
import glob
import re
import socket
import struct

ip2Location = []
ipAll = []

def readGeolocations():
	global ip2Location
	with open('IP2LOCATION.CSV') as f:
		for line in f.readlines():
			ip2Location.append(line.split(","))

def printAll(outAll):
	IPV4s = []
	for ip in ipAll:
		ipCountry = ip.split(',')
		IPV4s.append(ipCountry[0] + "," + ipCountry[2] + "," + ipCountry[3])
	ipAddresses = sorted(set(IPV4s))
	with open(outAll, "a+", encoding='utf8', errors='ignore') as outFile:
		outFile.write("IP,Code,Country\n")
		for ip in ipAddresses:
			outFile.write(ip)

def printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, start, end):
	global ipAll
	with open(outFile, "a+", encoding='utf8', errors='ignore') as outFile:
		for ipList in ip2Location[start:end]:
			if (int(ipList[0]) <= ipCheck <= int(ipList[1])):
				outFile.write( fileName.split("\\")[-3].strip('\n') + "," +
					fileName + "," + ip + "," + str(ipsCount.count(ip)) + "," + ipList[2] + "," + ipList[3][:-1] + "\n")
				ipAll.append(ip + "," + str(ipsCount.count(ip)) + "," + ipList[2] + "," + ipList[3][:-1] + "\n")
				break

def ipLookUp(fileName, ipsFound, ipsCount, outFile):
	for ip in ipsFound:
		try:
			ipCheck = struct.unpack('>I', socket.inet_aton(ip))[0]
			if (ipCheck <= int(ip2Location[73627][0])):
				if (ipCheck <= int(ip2Location[36813][0])):
					if (ipCheck <= int(ip2Location[18406][0])):
						if (ipCheck <= int(ip2Location[9203][0])):
							if (ipCheck <= int(ip2Location[4601][0])):
								if (ipCheck <= int(ip2Location[2300][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 0, 2300)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 2301, 4601)
							else:
								if (ipCheck <= int(ip2Location[6902][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 4602, 6902)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 6903, 9203)
						else:
							if (ipCheck <= int(ip2Location[13805][0])):
								if (ipCheck <= int(ip2Location[11504][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 9204, 11504)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 11505, 13805)
							else:
								if (ipCheck <= int(ip2Location[16106][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 13806, 16106)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 16107, 18406)
					else:
						if (ipCheck <= int(ip2Location[27610][0])):
							if (ipCheck <= int(ip2Location[23009][0])):
								if (ipCheck <= int(ip2Location[20707][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 18407, 20707)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 20708, 23009)
							else:
								if (ipCheck <= int(ip2Location[25310][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 23010, 25310)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 25311, 27610)
						else:
							if (ipCheck <= int(ip2Location[32211][0])):
								if (ipCheck <= int(ip2Location[29910][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 27611, 29910)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 29911, 32211)
							else:
								if (ipCheck <= int(ip2Location[34510][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 32212, 34510)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 34511, 36813)
				else:
					if (ipCheck <= int(ip2Location[55220][0])):
						if (ipCheck <= int(ip2Location[46017][0])):
							if (ipCheck <= int(ip2Location[41416][0])):
								if (ipCheck <= int(ip2Location[39114][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 36814, 39114)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 39115, 41416)
							else:
								if (ipCheck <= int(ip2Location[43717][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 41417, 43717)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 43718, 46017)
						else:
							if (ipCheck <= int(ip2Location[50619][0])):
								if (ipCheck <= int(ip2Location[48318][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 46018, 48318)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 48319, 50619)
							else:
								if (ipCheck <= int(ip2Location[52920][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 50620, 52920)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 52921, 55220)
					else:
						if (ipCheck <= int(ip2Location[64424][0])):
							if (ipCheck <= int(ip2Location[59822][0])):
								if (ipCheck <= int(ip2Location[57521][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 55221, 57521)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 57522, 59822)
							else:
								if (ipCheck <= int(ip2Location[62123][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 59823, 62123)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 62124, 64424)
						else:
							if (ipCheck <= int(ip2Location[69026][0])):
								if (ipCheck <= int(ip2Location[66725][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 64425, 66725)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 66726, 69026)
							else:
								if (ipCheck <= int(ip2Location[71327][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 69027, 71327)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 71328, 73627)
			else:
				if (ipCheck <= int(ip2Location[110440][0])):
					if (ipCheck <= int(ip2Location[92034][0])):
						if (ipCheck <= int(ip2Location[82831][0])):
							if (ipCheck <= int(ip2Location[78229][0])):
								if (ipCheck <= int(ip2Location[75928][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 73628, 75928)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 75929, 78229)
							else:
								if (ipCheck <= int(ip2Location[80530][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 78230, 80530)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 80531, 82831)
						else:
							if (ipCheck <= int(ip2Location[87433][0])):
								if (ipCheck <= int(ip2Location[85132][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 82832, 85132)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 85133, 87433)
							else:
								if (ipCheck <= int(ip2Location[89734][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 87434, 89734)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 89735, 92034)
					else:
						if (ipCheck <= int(ip2Location[101237][0])):
							if (ipCheck <= int(ip2Location[96636][0])):
								if (ipCheck <= int(ip2Location[94335][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 92035, 94335)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 94336, 96636)
							else:
								if (ipCheck <= int(ip2Location[98937][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 96637, 98937)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 98938, 101237)
						else:
							if (ipCheck <= int(ip2Location[105839][0])):
								if (ipCheck <= int(ip2Location[103538][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 101238, 103538)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 103539, 105839)
							else:
								if (ipCheck <= int(ip2Location[108140][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 105840, 108140)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 108141, 110440)
				else:
					if (ipCheck <= int(ip2Location[110441][0])):
						if (ipCheck <= int(ip2Location[119644][0])):
							if (ipCheck <= int(ip2Location[115042][0])):
								if (ipCheck <= int(ip2Location[112741][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 110441, 112741)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 112742, 115042)
							else:
								if (ipCheck <= int(ip2Location[117343][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 115043, 117343)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 117344, 119644)
						else:
							if (ipCheck <= int(ip2Location[124246][0])):
								if (ipCheck <= int(ip2Location[121945][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 119645, 121945)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 121946, 124246)
							else:
								if (ipCheck <= int(ip2Location[126547][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 124247, 126547)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 126548, 128848)
					else:
						if (ipCheck <= int(ip2Location[138051][0])):
							if (ipCheck <= int(ip2Location[133450][0])):
								if (ipCheck <= int(ip2Location[131149][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 128849, 131149)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 131150, 133450)
							else:
								if (ipCheck <= int(ip2Location[135751][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 133451, 135751)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 135752, 138051)
						else:
							if (ipCheck <= int(ip2Location[142652][0])):
								if (ipCheck <= int(ip2Location[140352][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 138052, 140352)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 140353, 142652)
							else:
								if (ipCheck <= int(ip2Location[144953][0])):
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 142653, 144953)
								else:
									printText(fileName, ipsFound, ipsCount, outFile, ip, ipCheck, 144954,
											  len(ip2Location))
		except socket.error:
			pass

def extractIPs(inputPath, outSystem, outAll):
	readGeolocations()
	for fileName in glob.iglob(inputPath + '**/**', recursive=True):
		print("IP Lookup: "+ fileName)
		try:
			with open(fileName, 'r', encoding='utf8', errors='ignore') as file:
				ipsFound = []
				ipsCount = []
				for line in file:
					text = line.rstrip()
					result = re.findall(
						r'(?:[1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]|[1-9][0-9]|1[0-9]'
						r'{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.'
						r'(?:[\d]{1,3})', text)
					if result:
						for IP in result:
							if len(IP.split('.')[0]) != 1:
								ipsCount.append(IP)
								if IP not in ipsFound:
									ipsFound.append(IP)
		except:
			continue
		ipLookUp(fileName, ipsFound, ipsCount, outSystem)
	printAll(outAll)

def main(inputPath, outSystem, outAll):
	with open(outSystem, "a+") as out:
		out.write("System,FileName,IP,Count,Code,Country\n")
	extractIPs(inputPath, outSystem, outAll)

if __name__ == "__main__":
	if len(sys.argv) == 4:
		main(sys.argv[1], sys.argv[2], sys.argv[3])
	else:
		print("Usage: ./ipLookup.py input-folder results-per-file.csv results-all-files.csv")
