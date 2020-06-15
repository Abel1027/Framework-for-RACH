import matplotlib.pyplot as plt
import os

if not os.path.isdir('graphs'): os.mkdir('graphs')

dirs = os.listdir()
dirs.remove('graphs')
dirs.remove('graphs_framework.py')

totalDevicesT = []
maxSymT = []
maxSCT = []
totalCollisionsNetworkT = []
totalCollisions24BandT = []
totalCollisionsT = []
totalEnergyNetworkT = []
totalEnergy24BandT = []
totalEnergyT = []
totalEnergyGNBT = []
totalTimeForRegistrationT = []
totalRegisteredByGNBT = []
totalRegisteredByRelayT = []
totalRegisteredDevicesT = []
totalDownlinkSCT = []
totalUplinkSCT = []
histogramT = []

for d in dirs:
	file = open(d + '/logs/best.log')
	lines = file.readlines()
	file.close()
	totalDevices = []
	maxSym = []
	maxSC = []
	totalCollisionsNetwork = []
	totalCollisions24Band = []
	totalCollisions = []
	totalEnergyNetwork = []
	totalEnergy24Band = []
	totalEnergy = []
	totalEnergyGNB = []
	totalTimeForRegistration = []
	totalRegisteredByGNB = []
	totalRegisteredByRelay = []
	totalRegisteredDevices = []
	totalDownlinkSC = []
	totalUplinkSC = []
	histogram = []
	for lineIndex in range(0, len(lines), 2):
		totalDevices.append(float(lines[lineIndex].split('|')[0]))
		maxSym.append(float(lines[lineIndex].split('|')[1]))
		maxSC.append(float(lines[lineIndex].split('|')[2]))
		totalCollisionsNetwork.append(float(lines[lineIndex].split('|')[3]))
		totalCollisions24Band.append(float(lines[lineIndex].split('|')[4]))
		totalCollisions.append(float(lines[lineIndex].split('|')[5]))
		totalEnergyNetwork.append(float(lines[lineIndex].split('|')[6]))
		totalEnergy24Band.append(float(lines[lineIndex].split('|')[7]))
		totalEnergy.append(float(lines[lineIndex].split('|')[8]))
		totalEnergyGNB.append(float(lines[lineIndex].split('|')[9]))
		totalTimeForRegistration.append(float(lines[lineIndex].split('|')[10]))
		totalTimeForRegistration[-1] = totalTimeForRegistration[-1]/1000
		totalRegisteredByGNB.append(float(lines[lineIndex].split('|')[11]))
		totalRegisteredByRelay.append(float(lines[lineIndex].split('|')[12]))
		totalRegisteredDevices.append(float(lines[lineIndex].split('|')[13]))
		totalDownlinkSC.append(float(lines[lineIndex].split('|')[14]))
		totalUplinkSC.append(float(lines[lineIndex].split('|')[15]))
	for lineIndex in range(1, len(lines), 2):
		histogram.append(lines[lineIndex].split('\n')[0])
	totalDevicesT.append(totalDevices)
	maxSymT.append(maxSym)
	maxSCT.append(maxSC)
	totalCollisionsNetworkT.append(totalCollisionsNetwork)
	totalCollisions24BandT.append(totalCollisions24Band)
	totalCollisionsT.append(totalCollisions)
	totalEnergyNetworkT.append(totalEnergyNetwork)
	totalEnergy24BandT.append(totalEnergy24Band)
	totalEnergyT.append(totalEnergy)
	totalEnergyGNBT.append(totalEnergyGNB)
	totalTimeForRegistrationT.append(totalTimeForRegistration)
	totalRegisteredByGNBT.append(totalRegisteredByGNB)
	totalRegisteredByRelayT.append(totalRegisteredByRelay)
	totalRegisteredDevicesT.append(totalRegisteredDevices)
	totalDownlinkSCT.append(totalDownlinkSC)
	totalUplinkSCT.append(totalUplinkSC)
	histogramT.append(histogram)

SMALL_SIZE = 8
MEDIUM_SIZE = 12
BIGGER_SIZE = 12

plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
mark = ['-d', '-o', '-v', '-s', '-x']

plt.figure(figsize=(10, 10))
for index, d in enumerate(dirs):
	if d == 'RACH':
		plt.plot(totalDevicesT[index], totalCollisions24BandT[index], '-d', label=d)
for index, d in enumerate(dirs):
	if d != 'RACH':
		plt.plot(totalDevicesT[index], totalCollisions24BandT[index], mark[index], label=d)
#plt.yscale('log')
plt.title('Collisions in the 2.4 GHz band')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Number of collisions')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('graphs/collisions_24.png')
plt.show()

plt.figure(figsize=(10, 10))
for index, d in enumerate(dirs):
	if d == 'RACH':
		plt.plot(totalDevicesT[index], totalCollisionsNetworkT[index], '-d', label=d)
for index, d in enumerate(dirs):
	if d != 'RACH':
		plt.plot(totalDevicesT[index], totalCollisionsNetworkT[index], mark[index], label=d)
#plt.yscale('log')
plt.title('Collisions in the Mobile Network band')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Number of collisions')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('graphs/collisions_network.png')
plt.show()

plt.figure(figsize=(10, 10))
for index, d in enumerate(dirs):
	if d == 'RACH':
		plt.plot(totalDevicesT[index], totalCollisionsT[index], '-d', label=d)
for index, d in enumerate(dirs):
	if d != 'RACH':
		plt.plot(totalDevicesT[index], totalCollisionsT[index], mark[index], label=d)
#plt.yscale('log')
plt.title('Total collisions (2.4 GHz band + Mobile Network band)')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Number of collisions')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('graphs/collisions_total.png')
plt.show()

plt.figure(figsize=(10, 10))
for index, d in enumerate(dirs):
	if d == 'RACH':
		plt.plot(totalDevicesT[index], totalEnergy24BandT[index], '-d', label=d)
for index, d in enumerate(dirs):
	if d != 'RACH':
		plt.plot(totalDevicesT[index], totalEnergy24BandT[index], mark[index], label=d)
#plt.yscale('log')
plt.title('Energy consumption in the 2.4 GHz band')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Energy consumption (units)')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('graphs/energy_24.png')
plt.show()

plt.figure(figsize=(10, 10))
for index, d in enumerate(dirs):
	if d == 'RACH':
		plt.plot(totalDevicesT[index], totalEnergyNetworkT[index], '-d', label=d)
for index, d in enumerate(dirs):
	if d != 'RACH':
		plt.plot(totalDevicesT[index], totalEnergyNetworkT[index], mark[index], label=d)
#plt.yscale('log')
plt.title('Energy consumption in the Mobile Network band')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Energy consumption (units)')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('graphs/energy_network.png')
plt.show()

plt.figure(figsize=(10, 10))
for index, d in enumerate(dirs):
	if d == 'RACH':
		plt.plot(totalDevicesT[index], totalEnergyT[index], '-d', label=d)
for index, d in enumerate(dirs):
	if d != 'RACH':
		plt.plot(totalDevicesT[index], totalEnergyT[index], mark[index], label=d)
#plt.yscale('log')
plt.title('Total energy consumption (2.4 GHz band + Mobile Network band)')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Energy consumption (units)')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('graphs/energy_total.png')
plt.show()

plt.figure(figsize=(10, 10))
for index, d in enumerate(dirs):
	if d == 'RACH':
		plt.plot(totalDevicesT[index], totalEnergyGNBT[index], '-d', label=d)
for index, d in enumerate(dirs):
	if d != 'RACH':
		plt.plot(totalDevicesT[index], totalEnergyGNBT[index], mark[index], label=d)
#plt.yscale('log')
plt.title('Energy consumption by the gNB')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Energy consumption (units)')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('graphs/energy_gNB.png')
plt.show()

plt.figure(figsize=(10, 10))
for index, d in enumerate(dirs):
	if d == 'RACH':
		plt.plot(totalDevicesT[index], totalTimeForRegistrationT[index], '-d', label=d)
for index, d in enumerate(dirs):
	if d != 'RACH':
		plt.plot(totalDevicesT[index], totalTimeForRegistrationT[index], mark[index], label=d)
plt.yscale('log')
plt.title('Total time for all device registering (ms)')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Time (ms)')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('graphs/time.png')
plt.show()

'''
plt.figure(figsize=(10, 10))
plt.subplot(2, 2, 1)
plt.plot(['12/5', '24/5', '36/5', '12/10', '24/10', '36/10', '12/14', '24/14', '36/14'], [totalDownlinkSC[0] for i in range(9)], label='RACH')
plt.plot(['12/5', '24/5', '36/5', '12/10', '24/10', '36/10', '12/14', '24/14', '36/14'], totalDownlinkSC6, label='Framework')
for index, value in enumerate(totalDownlinkSC6):
    plt.text(index, value, str(int(value)))
plt.title('Total resources offered for downlink (Subcarriers) - 100 devices')
plt.xlabel('Number of subcarriers/Number of symbols')
plt.ylabel('Number of subcarriers offered')
plt.legend(loc='upper center', shadow=True)
plt.grid(True)
##########
plt.subplot(2, 2, 2)
plt.plot(['12/5', '24/5', '36/5', '12/10', '24/10', '36/10', '12/14', '24/14', '36/14'], [totalUplinkSC[0] for i in range(9)], label='RACH')
plt.plot(['12/5', '24/5', '36/5', '12/10', '24/10', '36/10', '12/14', '24/14', '36/14'], totalUplinkSC6, label='Framework')
for index, value in enumerate(totalUplinkSC6):
    plt.text(index, value, str(int(value)))
plt.title('Total resources offered for uplink (Subcarriers) - 100 devices')
plt.xlabel('Number of subcarriers/Number of symbols')
plt.ylabel('Number of subcarriers offered')
plt.legend(loc='upper center', shadow=True)
plt.grid(True)
##########
plt.subplot(2, 2, 3)
plt.plot(['12/5', '24/5', '36/5', '12/10', '24/10', '36/10', '12/14', '24/14', '36/14'], [totalDownlinkSC[6] for i in range(9)], label='RACH')
plt.plot(['12/5', '24/5', '36/5', '12/10', '24/10', '36/10', '12/14', '24/14', '36/14'], totalDownlinkSC7, label='Framework')
for index, value in enumerate(totalDownlinkSC7):
    plt.text(index, value, str(int(value)))
plt.title('Total resources offered for downlink (Subcarriers) - 1000 devices')
plt.xlabel('Number of subcarriers/Number of symbols')
plt.ylabel('Number of subcarriers offered')
plt.legend(loc='upper center', shadow=True)
plt.grid(True)
##########
plt.subplot(2, 2, 4)
plt.plot(['12/5', '24/5', '36/5', '12/10', '24/10', '36/10', '12/14', '24/14', '36/14'], [totalUplinkSC[6] for i in range(9)], label='RACH')
plt.plot(['12/5', '24/5', '36/5', '12/10', '24/10', '36/10', '12/14', '24/14', '36/14'], totalUplinkSC7, label='Framework')
for index, value in enumerate(totalUplinkSC7):
    plt.text(index, value, str(int(value)))
plt.title('Total resources offered for uplink (Subcarriers) - 1000 devices')
plt.xlabel('Number of subcarriers/Number of symbols')
plt.ylabel('Number of subcarriers offered')
plt.legend(loc='upper center', shadow=True)
plt.grid(True)
plt.savefig('graphs/resources_uplink_100_1000_devices.png')
plt.show()
##########
'''