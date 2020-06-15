import matplotlib.pyplot as plt
import os

if not os.path.isdir('graphs'): os.mkdir('graphs')

file = open('logs/01.log')
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

file = open('logs/02.log')
lines = file.readlines()
file.close()
totalDevices2 = []
maxSym2 = []
maxSC2 = []
totalCollisionsNetwork2 = []
totalCollisions24Band2 = []
totalCollisions2 = []
totalEnergyNetwork2 = []
totalEnergy24Band2 = []
totalEnergy2 = []
totalEnergyGNB2 = []
totalTimeForRegistration2 = []
totalRegisteredByGNB2 = []
totalRegisteredByRelay2 = []
totalRegisteredDevices2 = []
totalDownlinkSC2 = []
totalUplinkSC2 = []
histogram2 = []
for lineIndex in range(0, len(lines), 2):
	totalDevices2.append(float(lines[lineIndex].split('|')[0]))
	maxSym2.append(float(lines[lineIndex].split('|')[1]))
	maxSC2.append(float(lines[lineIndex].split('|')[2]))
	totalCollisionsNetwork2.append(float(lines[lineIndex].split('|')[3]))
	totalCollisions24Band2.append(float(lines[lineIndex].split('|')[4]))
	totalCollisions2.append(float(lines[lineIndex].split('|')[5]))
	totalEnergyNetwork2.append(float(lines[lineIndex].split('|')[6]))
	totalEnergy24Band2.append(float(lines[lineIndex].split('|')[7]))
	totalEnergy2.append(float(lines[lineIndex].split('|')[8]))
	totalEnergyGNB2.append(float(lines[lineIndex].split('|')[9]))
	totalTimeForRegistration2.append(float(lines[lineIndex].split('|')[10]))
	totalTimeForRegistration2[-1] = totalTimeForRegistration2[-1]/1000
	totalRegisteredByGNB2.append(float(lines[lineIndex].split('|')[11]))
	totalRegisteredByRelay2.append(float(lines[lineIndex].split('|')[12]))
	totalRegisteredDevices2.append(float(lines[lineIndex].split('|')[13]))
	totalDownlinkSC2.append(float(lines[lineIndex].split('|')[14]))
	totalUplinkSC2.append(float(lines[lineIndex].split('|')[15]))
for lineIndex in range(1, len(lines), 2):
	histogram2.append(lines[lineIndex].split('\n')[0])

file = open('logs/03.log')
lines = file.readlines()
file.close()
totalDevices3 = []
maxSym3 = []
maxSC3 = []
totalCollisionsNetwork3 = []
totalCollisions24Band3 = []
totalCollisions3 = []
totalEnergyNetwork3 = []
totalEnergy24Band3 = []
totalEnergy3 = []
totalEnergyGNB3 = []
totalTimeForRegistration3 = []
totalRegisteredByGNB3 = []
totalRegisteredByRelay3 = []
totalRegisteredDevices3 = []
totalDownlinkSC3 = []
totalUplinkSC3 = []
histogram3 = []
for lineIndex in range(0, len(lines), 2):
	totalDevices3.append(float(lines[lineIndex].split('|')[0]))
	maxSym3.append(float(lines[lineIndex].split('|')[1]))
	maxSC3.append(float(lines[lineIndex].split('|')[2]))
	totalCollisionsNetwork3.append(float(lines[lineIndex].split('|')[3]))
	totalCollisions24Band3.append(float(lines[lineIndex].split('|')[4]))
	totalCollisions3.append(float(lines[lineIndex].split('|')[5]))
	totalEnergyNetwork3.append(float(lines[lineIndex].split('|')[6]))
	totalEnergy24Band3.append(float(lines[lineIndex].split('|')[7]))
	totalEnergy3.append(float(lines[lineIndex].split('|')[8]))
	totalEnergyGNB3.append(float(lines[lineIndex].split('|')[9]))
	totalTimeForRegistration3.append(float(lines[lineIndex].split('|')[10]))
	totalTimeForRegistration3[-1] = totalTimeForRegistration3[-1]/1000
	totalRegisteredByGNB3.append(float(lines[lineIndex].split('|')[11]))
	totalRegisteredByRelay3.append(float(lines[lineIndex].split('|')[12]))
	totalRegisteredDevices3.append(float(lines[lineIndex].split('|')[13]))
	totalDownlinkSC3.append(float(lines[lineIndex].split('|')[14]))
	totalUplinkSC3.append(float(lines[lineIndex].split('|')[15]))
for lineIndex in range(1, len(lines), 2):
	histogram3.append(lines[lineIndex].split('\n')[0])

file = open('logs/04.log')
lines = file.readlines()
file.close()
totalDevices4 = []
maxSym4 = []
maxSC4 = []
totalCollisionsNetwork4 = []
totalCollisions24Band4 = []
totalCollisions4 = []
totalEnergyNetwork4 = []
totalEnergy24Band4 = []
totalEnergy4 = []
totalEnergyGNB4 = []
totalTimeForRegistration4 = []
totalRegisteredByGNB4 = []
totalRegisteredByRelay4 = []
totalRegisteredDevices4 = []
totalDownlinkSC4 = []
totalUplinkSC4 = []
histogram4= []
for lineIndex in range(0, len(lines), 2):
	totalDevices4.append(float(lines[lineIndex].split('|')[0]))
	maxSym4.append(float(lines[lineIndex].split('|')[1]))
	maxSC4.append(float(lines[lineIndex].split('|')[2]))
	totalCollisionsNetwork4.append(float(lines[lineIndex].split('|')[3]))
	totalCollisions24Band4.append(float(lines[lineIndex].split('|')[4]))
	totalCollisions4.append(float(lines[lineIndex].split('|')[5]))
	totalEnergyNetwork4.append(float(lines[lineIndex].split('|')[6]))
	totalEnergy24Band4.append(float(lines[lineIndex].split('|')[7]))
	totalEnergy4.append(float(lines[lineIndex].split('|')[8]))
	totalEnergyGNB4.append(float(lines[lineIndex].split('|')[9]))
	totalTimeForRegistration4.append(float(lines[lineIndex].split('|')[10]))
	totalTimeForRegistration4[-1] = totalTimeForRegistration4[-1]/1000
	totalRegisteredByGNB4.append(float(lines[lineIndex].split('|')[11]))
	totalRegisteredByRelay4.append(float(lines[lineIndex].split('|')[12]))
	totalRegisteredDevices4.append(float(lines[lineIndex].split('|')[13]))
	totalDownlinkSC4.append(float(lines[lineIndex].split('|')[14]))
	totalUplinkSC4.append(float(lines[lineIndex].split('|')[15]))
for lineIndex in range(1, len(lines), 2):
	histogram4.append(lines[lineIndex].split('\n')[0])

file = open('logs/05.log')
lines = file.readlines()
file.close()
totalDevices5 = []
maxSym5 = []
maxSC5 = []
totalCollisionsNetwork5 = []
totalCollisions24Band5 = []
totalCollisions5 = []
totalEnergyNetwork5 = []
totalEnergy24Band5 = []
totalEnergy5 = []
totalEnergyGNB5 = []
totalTimeForRegistration5 = []
totalRegisteredByGNB5 = []
totalRegisteredByRelay5 = []
totalRegisteredDevices5 = []
totalDownlinkSC5 = []
totalUplinkSC5 = []
histogram5 = []
for lineIndex in range(0, len(lines), 2):
	totalDevices5.append(float(lines[lineIndex].split('|')[0]))
	maxSym5.append(float(lines[lineIndex].split('|')[1]))
	maxSC5.append(float(lines[lineIndex].split('|')[2]))
	totalCollisionsNetwork5.append(float(lines[lineIndex].split('|')[3]))
	totalCollisions24Band5.append(float(lines[lineIndex].split('|')[4]))
	totalCollisions5.append(float(lines[lineIndex].split('|')[5]))
	totalEnergyNetwork5.append(float(lines[lineIndex].split('|')[6]))
	totalEnergy24Band5.append(float(lines[lineIndex].split('|')[7]))
	totalEnergy5.append(float(lines[lineIndex].split('|')[8]))
	totalEnergyGNB5.append(float(lines[lineIndex].split('|')[9]))
	totalTimeForRegistration5.append(float(lines[lineIndex].split('|')[10]))
	totalTimeForRegistration5[-1] = totalTimeForRegistration5[-1]/1000
	totalRegisteredByGNB5.append(float(lines[lineIndex].split('|')[11]))
	totalRegisteredByRelay5.append(float(lines[lineIndex].split('|')[12]))
	totalRegisteredDevices5.append(float(lines[lineIndex].split('|')[13]))
	totalDownlinkSC5.append(float(lines[lineIndex].split('|')[14]))
	totalUplinkSC5.append(float(lines[lineIndex].split('|')[15]))
for lineIndex in range(1, len(lines), 2):
	histogram5.append(lines[lineIndex].split('\n')[0])
'''
file = open('logs/06.log')
lines = file.readlines()
file.close()
totalDevices6 = []
maxSym6 = []
maxSC6 = []
totalCollisionsNetwork6 = []
totalCollisions24Band6 = []
totalCollisions6 = []
totalEnergyNetwork6 = []
totalEnergy24Band6 = []
totalEnergy6 = []
totalEnergyGNB6 = []
totalTimeForRegistration6 = []
totalRegisteredByGNB6 = []
totalRegisteredByRelay6 = []
totalRegisteredDevices6 = []
totalDownlinkSC6 = []
totalUplinkSC6 = []
histogram6 = []
for lineIndex in range(0, len(lines), 2):
	totalDevices6.append(float(lines[lineIndex].split('|')[0]))
	maxSym6.append(float(lines[lineIndex].split('|')[1]))
	maxSC6.append(float(lines[lineIndex].split('|')[2]))
	totalCollisionsNetwork6.append(float(lines[lineIndex].split('|')[3]))
	totalCollisions24Band6.append(float(lines[lineIndex].split('|')[4]))
	totalCollisions6.append(float(lines[lineIndex].split('|')[5]))
	totalEnergyNetwork6.append(float(lines[lineIndex].split('|')[6]))
	totalEnergy24Band6.append(float(lines[lineIndex].split('|')[7]))
	totalEnergy6.append(float(lines[lineIndex].split('|')[8]))
	totalEnergyGNB6.append(float(lines[lineIndex].split('|')[9]))
	totalTimeForRegistration6.append(float(lines[lineIndex].split('|')[10]))
	totalTimeForRegistration6[-1] = totalTimeForRegistration6[-1]/1000
	totalRegisteredByGNB6.append(float(lines[lineIndex].split('|')[11]))
	totalRegisteredByRelay6.append(float(lines[lineIndex].split('|')[12]))
	totalRegisteredDevices6.append(float(lines[lineIndex].split('|')[13]))
	totalDownlinkSC6.append(float(lines[lineIndex].split('|')[14]))
	totalUplinkSC6.append(float(lines[lineIndex].split('|')[15]))
for lineIndex in range(1, len(lines), 2):
	histogram6.append(lines[lineIndex].split('\n')[0])

file = open('logs/07.log')
lines = file.readlines()
file.close()
totalDevices7 = []
maxSym7 = []
maxSC7 = []
totalCollisionsNetwork7 = []
totalCollisions24Band7 = []
totalCollisions7 = []
totalEnergyNetwork7 = []
totalEnergy24Band7 = []
totalEnergy7 = []
totalEnergyGNB7 = []
totalTimeForRegistration7 = []
totalRegisteredByGNB7 = []
totalRegisteredByRelay7 = []
totalRegisteredDevices7 = []
totalDownlinkSC7 = []
totalUplinkSC7 = []
histogram7 = []
for lineIndex in range(0, len(lines), 2):
	totalDevices7.append(float(lines[lineIndex].split('|')[0]))
	maxSym7.append(float(lines[lineIndex].split('|')[1]))
	maxSC7.append(float(lines[lineIndex].split('|')[2]))
	totalCollisionsNetwork7.append(float(lines[lineIndex].split('|')[3]))
	totalCollisions24Band7.append(float(lines[lineIndex].split('|')[4]))
	totalCollisions7.append(float(lines[lineIndex].split('|')[5]))
	totalEnergyNetwork7.append(float(lines[lineIndex].split('|')[6]))
	totalEnergy24Band7.append(float(lines[lineIndex].split('|')[7]))
	totalEnergy7.append(float(lines[lineIndex].split('|')[8]))
	totalEnergyGNB7.append(float(lines[lineIndex].split('|')[9]))
	totalTimeForRegistration7.append(float(lines[lineIndex].split('|')[10]))
	totalTimeForRegistration7[-1] = totalTimeForRegistration7[-1]/1000
	totalRegisteredByGNB7.append(float(lines[lineIndex].split('|')[11]))
	totalRegisteredByRelay7.append(float(lines[lineIndex].split('|')[12]))
	totalRegisteredDevices7.append(float(lines[lineIndex].split('|')[13]))
	totalDownlinkSC7.append(float(lines[lineIndex].split('|')[14]))
	totalUplinkSC7.append(float(lines[lineIndex].split('|')[15]))
for lineIndex in range(1, len(lines), 2):
	histogram7.append(lines[lineIndex].split('\n')[0])
SMALL_SIZE = 5.7
MEDIUM_SIZE = 8
BIGGER_SIZE = 12
'''
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

plt.figure(figsize=(10, 10))
plt.subplot(2, 1, 1)
plt.plot(totalDevices, totalCollisions24Band, '-d', label='RACH')
plt.plot(totalDevices2, totalCollisions24Band2, '-o', label='RACH + Framework (after SIB1)')
plt.plot(totalDevices2, totalCollisions24Band3, '-v', label='RACH + Framework (before SIB1)')
plt.plot(totalDevices2, totalCollisions24Band4, '-s', label='RACH + Framework (after SIB1 + frequency assigned by gNB)')
plt.plot(totalDevices2, totalCollisions24Band5, '-x', label='RACH + Framework (before SIB1 + frequency assigned by gNB)')
plt.yscale('log')
plt.title('Collisions in the 2.4 GHz band')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Number of collisions')
plt.legend(loc='upper center', shadow=True)
plt.grid(True)
##########
plt.subplot(2, 2, 3)
plt.plot(totalDevices[:4], totalCollisions24Band[:4], '-d')
plt.plot(totalDevices2[:4], totalCollisions24Band2[:4], '-o')
plt.plot(totalDevices2[:4], totalCollisions24Band3[:4], '-v')
plt.plot(totalDevices2[:4], totalCollisions24Band4[:4], '-s')
plt.plot(totalDevices2[:4], totalCollisions24Band5[:4], '-x')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Number of collisions')
plt.grid(True)
##########
plt.subplot(2, 2, 4)
plt.plot(totalDevices[3:], totalCollisions24Band[3:], '-d')
plt.plot(totalDevices2[3:], totalCollisions24Band2[3:], '-o')
plt.plot(totalDevices2[3:], totalCollisions24Band3[3:], '-v')
plt.plot(totalDevices2[3:], totalCollisions24Band4[3:], '-s')
plt.plot(totalDevices2[3:], totalCollisions24Band5[3:], '-x')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.grid(True)
plt.savefig('graphs/collisions_24.png')
plt.show()

plt.figure(figsize=(10, 10))
plt.subplot(2, 1, 1)
plt.plot(totalDevices, totalCollisionsNetwork, '-d', label='RACH')
plt.plot(totalDevices2, totalCollisionsNetwork2, '-o', label='RACH + Framework (after SIB1)')
plt.plot(totalDevices2, totalCollisionsNetwork3, '-v', label='RACH + Framework (before SIB1)')
plt.plot(totalDevices2, totalCollisionsNetwork4, '-s', label='RACH + Framework (after SIB1 + frequency assigned by gNB)')
plt.plot(totalDevices2, totalCollisionsNetwork5, '-x', label='RACH + Framework (before SIB1 + frequency assigned by gNB)')
plt.yscale('log')
plt.title('Collisions in the Mobile Network band')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Number of collisions')
plt.legend(loc='upper center', shadow=True)
plt.grid(True)
##########
plt.subplot(2, 2, 3)
plt.plot(totalDevices[:5], totalCollisionsNetwork[:5], '-d')
plt.plot(totalDevices2[:5], totalCollisionsNetwork2[:5], '-o')
plt.plot(totalDevices2[:5], totalCollisionsNetwork3[:5], '-v')
plt.plot(totalDevices2[:5], totalCollisionsNetwork4[:5], '-s')
plt.plot(totalDevices2[:5], totalCollisionsNetwork5[:5], '-x')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Number of collisions')
plt.grid(True)
##########
plt.subplot(2, 2, 4)
plt.plot(totalDevices[4:], totalCollisionsNetwork[4:], '-d')
plt.plot(totalDevices2[4:], totalCollisionsNetwork2[4:], '-o')
plt.plot(totalDevices2[4:], totalCollisionsNetwork3[4:], '-v')
plt.plot(totalDevices2[4:], totalCollisionsNetwork4[4:], '-s')
plt.plot(totalDevices2[4:], totalCollisionsNetwork5[4:], '-x')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.grid(True)
plt.savefig('graphs/collisions_network.png')
plt.show()

plt.figure(figsize=(10, 10))
plt.subplot(2, 1, 1)
plt.plot(totalDevices, totalCollisions, '-d', label='RACH')
plt.plot(totalDevices2, totalCollisions2, '-o', label='RACH + Framework (after SIB1)')
plt.plot(totalDevices2, totalCollisions3, '-v', label='RACH + Framework (before SIB1)')
plt.plot(totalDevices2, totalCollisions4, '-s', label='RACH + Framework (after SIB1 + frequency assigned by gNB)')
plt.plot(totalDevices2, totalCollisions5, '-x', label='RACH + Framework (before SIB1 + frequency assigned by gNB)')
plt.yscale('log')
plt.title('Total collisions (2.4 GHz band + Mobile Network band)')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Number of collisions')
plt.legend(loc='upper center', shadow=True)
plt.grid(True)
##########
plt.subplot(2, 2, 3)
plt.plot(totalDevices[:5], totalCollisions[:5], '-d')
plt.plot(totalDevices2[:5], totalCollisions2[:5], '-o')
plt.plot(totalDevices2[:5], totalCollisions3[:5], '-v')
plt.plot(totalDevices2[:5], totalCollisions4[:5], '-s')
plt.plot(totalDevices2[:5], totalCollisions5[:5], '-x')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Number of collisions')
plt.grid(True)
##########
plt.subplot(2, 2, 4)
plt.plot(totalDevices[4:], totalCollisions[4:], '-d')
plt.plot(totalDevices2[4:], totalCollisions2[4:], '-o')
plt.plot(totalDevices2[4:], totalCollisions3[4:], '-v')
plt.plot(totalDevices2[4:], totalCollisions4[4:], '-s')
plt.plot(totalDevices2[4:], totalCollisions5[4:], '-x')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.grid(True)
plt.savefig('graphs/collisions_total.png')
plt.show()

plt.figure(figsize=(10, 10))
plt.subplot(2, 1, 1)
plt.plot(totalDevices, totalEnergy24Band, '-d', label='RACH')
plt.plot(totalDevices2, totalEnergy24Band2, '-o', label='RACH + Framework (after SIB1)')
plt.plot(totalDevices2, totalEnergy24Band3, '-v', label='RACH + Framework (before SIB1)')
plt.plot(totalDevices2, totalEnergy24Band4, '-s', label='RACH + Framework (after SIB1 + frequency assigned by gNB)')
plt.plot(totalDevices2, totalEnergy24Band5, '-x', label='RACH + Framework (before SIB1 + frequency assigned by gNB)')
plt.yscale('log')
plt.title('Energy consumption in the 2.4 GHz band')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Energy consumption (units)')
plt.legend(loc='upper center', shadow=True)
plt.grid(True)
##########
plt.subplot(2, 2, 3)
plt.plot(totalDevices[:5], totalEnergy24Band[:5], '-d')
plt.plot(totalDevices2[:5], totalEnergy24Band2[:5], '-o')
plt.plot(totalDevices2[:5], totalEnergy24Band3[:5], '-v')
plt.plot(totalDevices2[:5], totalEnergy24Band4[:5], '-s')
plt.plot(totalDevices2[:5], totalEnergy24Band5[:5], '-x')
plt.ylabel('Energy consumption (units)')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.grid(True)
##########
plt.subplot(2, 2, 4)
plt.plot(totalDevices[4:], totalEnergy24Band[4:], '-d')
plt.plot(totalDevices2[4:], totalEnergy24Band2[4:], '-o')
plt.plot(totalDevices2[4:], totalEnergy24Band3[4:], '-v')
plt.plot(totalDevices2[4:], totalEnergy24Band4[4:], '-s')
plt.plot(totalDevices2[4:], totalEnergy24Band5[4:], '-x')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.grid(True)
plt.savefig('graphs/energy_24.png')
plt.show()

plt.figure(figsize=(10, 10))
plt.subplot(2, 1, 1)
plt.plot(totalDevices, totalEnergyNetwork, '-d', label='RACH')
plt.plot(totalDevices2, totalEnergyNetwork2, '-o', label='RACH + Framework (after SIB1)')
plt.plot(totalDevices2, totalEnergyNetwork3, '-v', label='RACH + Framework (before SIB1)')
plt.plot(totalDevices2, totalEnergyNetwork4, '-s', label='RACH + Framework (after SIB1 + frequency assigned by gNB)')
plt.plot(totalDevices2, totalEnergyNetwork5, '-x', label='RACH + Framework (before SIB1 + frequency assigned by gNB)')
plt.yscale('log')
plt.title('Energy consumption in the Mobile Network band')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Energy consumption (units)')
plt.legend(loc='upper center', shadow=True)
plt.grid(True)
##########
plt.subplot(2, 2, 3)
plt.plot(totalDevices[:5], totalEnergyNetwork[:5], '-d')
plt.plot(totalDevices2[:5], totalEnergyNetwork2[:5], '-o')
plt.plot(totalDevices2[:5], totalEnergyNetwork3[:5], '-v')
plt.plot(totalDevices2[:5], totalEnergyNetwork4[:5], '-s')
plt.plot(totalDevices2[:5], totalEnergyNetwork5[:5], '-x')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Energy consumption (units)')
plt.grid(True)
##########
plt.subplot(2, 2, 4)
plt.plot(totalDevices[4:], totalEnergyNetwork[4:], '-d')
plt.plot(totalDevices2[4:], totalEnergyNetwork2[4:], '-o')
plt.plot(totalDevices2[4:], totalEnergyNetwork3[4:], '-v')
plt.plot(totalDevices2[4:], totalEnergyNetwork4[4:], '-s')
plt.plot(totalDevices2[4:], totalEnergyNetwork5[4:], '-x')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.grid(True)
plt.savefig('graphs/energy_network.png')
plt.show()

plt.figure(figsize=(10, 10))
plt.subplot(2, 1, 1)
plt.plot(totalDevices, totalEnergy, '-d', label='RACH')
plt.plot(totalDevices2, totalEnergy2, '-o', label='RACH + Framework (after SIB1)')
plt.plot(totalDevices2, totalEnergy3, '-v', label='RACH + Framework (before SIB1)')
plt.plot(totalDevices2, totalEnergy4, '-s', label='RACH + Framework (after SIB1 + frequency assigned by gNB)')
plt.plot(totalDevices2, totalEnergy5, '-x', label='RACH + Framework (before SIB1 + frequency assigned by gNB)')
plt.yscale('log')
plt.title('Total energy consumption (2.4 GHz band + Mobile Network band)')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Energy consumption (units)')
plt.legend(loc='upper center', shadow=True)
plt.grid(True)
##########
plt.subplot(2, 2, 3)
plt.plot(totalDevices[:5], totalEnergy[:5], '-d')
plt.plot(totalDevices2[:5], totalEnergy2[:5], '-o')
plt.plot(totalDevices2[:5], totalEnergy3[:5], '-v')
plt.plot(totalDevices2[:5], totalEnergy4[:5], '-s')
plt.plot(totalDevices2[:5], totalEnergy5[:5], '-x')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Energy consumption (units)')
plt.grid(True)
##########
plt.subplot(2, 2, 4)
plt.plot(totalDevices[4:], totalEnergy[4:], '-d')
plt.plot(totalDevices2[4:], totalEnergy2[4:], '-o')
plt.plot(totalDevices2[4:], totalEnergy3[4:], '-v')
plt.plot(totalDevices2[4:], totalEnergy4[4:], '-s')
plt.plot(totalDevices2[4:], totalEnergy5[4:], '-x')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.grid(True)
plt.savefig('graphs/energy_total.png')
plt.show()
#__________________________
plt.figure(figsize=(10, 10))
#plt.plot(totalDevices, totalEnergy, '-d', label='RACH')
plt.plot(totalDevices2, totalEnergy2, '-o', label='Framework (after SIB1)')
plt.plot(totalDevices2, totalEnergy3, '-v', label='Framework (before SIB1)')
plt.plot(totalDevices2, totalEnergy4, '-s', label='Framework (after SIB1 + frequency assigned by gNB)')
plt.plot(totalDevices2, totalEnergy5, '-x', label='Framework (before SIB1 + frequency assigned by gNB)')
#plt.yscale('log')
plt.title('Total energy consumption (2.4 GHz band + Mobile Network band)')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Energy consumption (units)')
plt.legend(loc='best', shadow=True)
plt.grid(True)
plt.savefig('graphs/energyTOTAL.png')
plt.show()

plt.figure(figsize=(10, 10))
plt.subplot(2, 1, 1)
plt.plot(totalDevices, totalEnergyGNB, '-d', label='RACH')
plt.plot(totalDevices2, totalEnergyGNB2, '-o', label='RACH + Framework (after SIB1)')
plt.plot(totalDevices2, totalEnergyGNB3, '-v', label='RACH + Framework (before SIB1)')
plt.plot(totalDevices2, totalEnergyGNB4, '-s', label='RACH + Framework (after SIB1 + frequency assigned by gNB)')
plt.plot(totalDevices2, totalEnergyGNB5, '-x', label='RACH + Framework (before SIB1 + frequency assigned by gNB)')
plt.yscale('log')
plt.title('Energy consumption by the gNB')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Energy consumption (units)')
plt.legend(loc='lower right', shadow=True)
plt.grid(True)
##########
plt.subplot(2, 2, 3)
plt.plot(totalDevices[:5], totalEnergyGNB[:5], '-d')
plt.plot(totalDevices2[:5], totalEnergyGNB2[:5], '-o')
plt.plot(totalDevices2[:5], totalEnergyGNB3[:5], '-v')
plt.plot(totalDevices2[:5], totalEnergyGNB4[:5], '-s')
plt.plot(totalDevices2[:5], totalEnergyGNB5[:5], '-x')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Energy consumption (units)')
plt.grid(True)
##########
plt.subplot(2, 2, 4)
plt.plot(totalDevices[4:], totalEnergyGNB[4:], '-d')
plt.plot(totalDevices2[4:], totalEnergyGNB2[4:], '-o')
plt.plot(totalDevices2[4:], totalEnergyGNB3[4:], '-v')
plt.plot(totalDevices2[4:], totalEnergyGNB4[4:], '-s')
plt.plot(totalDevices2[4:], totalEnergyGNB5[4:], '-x')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.grid(True)
plt.savefig('graphs/energy_gNB.png')
plt.show()

plt.figure(figsize=(10, 10))
plt.subplot(4, 1, 1)
plt.plot(totalDevices, totalTimeForRegistration, '-d', label='RACH')
plt.plot(totalDevices2, totalTimeForRegistration2, '-o', label='RACH + Framework (after SIB1)')
plt.plot(totalDevices2, totalTimeForRegistration3, '-v', label='RACH + Framework (before SIB1)')
plt.plot(totalDevices2, totalTimeForRegistration4, '-s', label='RACH + Framework (after SIB1 + frequency assigned by gNB)')
plt.plot(totalDevices2, totalTimeForRegistration5, '-x', label='RACH + Framework (before SIB1 + frequency assigned by gNB)')
plt.yscale('log')
plt.title('Total time for all device registering (ms)')
plt.ylabel('Time (ms)')
plt.legend(loc='upper left', shadow=True)
plt.grid(True)
##########
plt.subplot(4, 2, 3)
plt.plot(totalDevices[:2], totalTimeForRegistration[:2], '-d')
plt.plot(totalDevices2[:2], totalTimeForRegistration2[:2], '-o')
plt.plot(totalDevices2[:2], totalTimeForRegistration3[:2], '-v')
plt.plot(totalDevices2[:2], totalTimeForRegistration4[:2], '-s')
plt.plot(totalDevices2[:2], totalTimeForRegistration5[:2], '-x')
plt.ylabel('Time (ms)')
plt.grid(True)
##########
plt.subplot(4, 2, 4)
plt.plot(totalDevices[1:3], totalTimeForRegistration[1:3], '-d')
plt.plot(totalDevices2[1:3], totalTimeForRegistration2[1:3], '-o')
plt.plot(totalDevices2[1:3], totalTimeForRegistration3[1:3], '-v')
plt.plot(totalDevices2[1:3], totalTimeForRegistration4[1:3], '-s')
plt.plot(totalDevices2[1:3], totalTimeForRegistration5[1:3], '-x')
plt.grid(True)
##########
plt.subplot(4, 2, 5)
plt.plot(totalDevices[2:4], totalTimeForRegistration[2:4], '-d')
plt.plot(totalDevices2[2:4], totalTimeForRegistration2[2:4], '-o')
plt.plot(totalDevices2[2:4], totalTimeForRegistration3[2:4], '-v')
plt.plot(totalDevices2[2:4], totalTimeForRegistration4[2:4], '-s')
plt.plot(totalDevices2[2:4], totalTimeForRegistration5[2:4], '-x')
plt.ylabel('Time (ms)')
plt.grid(True)
##########
plt.subplot(4, 2, 6)
plt.plot(totalDevices[3:5], totalTimeForRegistration[3:5], '-d')
plt.plot(totalDevices2[3:5], totalTimeForRegistration2[3:5], '-o')
plt.plot(totalDevices2[3:5], totalTimeForRegistration3[3:5], '-v')
plt.plot(totalDevices2[3:5], totalTimeForRegistration4[3:5], '-s')
plt.plot(totalDevices2[3:5], totalTimeForRegistration5[3:5], '-x')
plt.grid(True)
##########
plt.subplot(4, 2, 7)
plt.plot(totalDevices[4:6], totalTimeForRegistration[4:6], '-d')
plt.plot(totalDevices2[4:6], totalTimeForRegistration2[4:6], '-o')
plt.plot(totalDevices2[4:6], totalTimeForRegistration3[4:6], '-v')
plt.plot(totalDevices2[4:6], totalTimeForRegistration4[4:6], '-s')
plt.plot(totalDevices2[4:6], totalTimeForRegistration5[4:6], '-x')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Time (ms)')
plt.grid(True)
##########
plt.subplot(4, 2, 8)
plt.plot(totalDevices[5:], totalTimeForRegistration[5:], '-d')
plt.plot(totalDevices2[5:], totalTimeForRegistration2[5:], '-o')
plt.plot(totalDevices2[5:], totalTimeForRegistration3[5:], '-v')
plt.plot(totalDevices2[5:], totalTimeForRegistration4[5:], '-s')
plt.plot(totalDevices2[5:], totalTimeForRegistration5[5:], '-x')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.grid(True)
plt.savefig('graphs/time.png')
plt.show()
#___________________________
plt.figure(figsize=(10, 10))
#plt.plot(totalDevices, totalTimeForRegistration, '-d', label='RACH')
plt.plot(totalDevices2, totalTimeForRegistration2, '-o', label='Framework (after SIB1)')
plt.plot(totalDevices2, totalTimeForRegistration3, '-v', label='Framework (before SIB1)')
plt.plot(totalDevices2, totalTimeForRegistration4, '-s', label='Framework (after SIB1 + frequency assigned by gNB)')
plt.plot(totalDevices2, totalTimeForRegistration5, '-x', label='Framework (before SIB1 + frequency assigned by gNB)')
#plt.yscale('log')
plt.title('Total time for all device registering (ms)')
plt.ylabel('Time (ms)')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.legend(loc='upper left', shadow=True)
plt.grid(True)
plt.savefig('graphs/timeTOTAL.png')
plt.show()

plt.figure(figsize=(10, 10))
plt.subplot(4, 1, 1)
plt.plot(totalDevices2, totalTimeForRegistration2, '-o', label='RACH + Framework (after SIB1)')
plt.plot(totalDevices2, totalTimeForRegistration3, '-v', label='RACH + Framework (before SIB1)')
plt.plot(totalDevices2, totalTimeForRegistration4, '-s', label='RACH + Framework (after SIB1 + frequency assigned by gNB)')
plt.plot(totalDevices2, totalTimeForRegistration5, '-x', label='RACH + Framework (before SIB1 + frequency assigned by gNB)')
plt.yscale('log')
plt.title('Total time for all device registering (ms) - Framework')
plt.ylabel('Time (ms)')
plt.legend(loc='lower right', shadow=True)
plt.grid(True)
##########
plt.subplot(4, 2, 3)
plt.plot(totalDevices2[:2], totalTimeForRegistration2[:2], '-o')
plt.plot(totalDevices2[:2], totalTimeForRegistration3[:2], '-v')
plt.plot(totalDevices2[:2], totalTimeForRegistration4[:2], '-s')
plt.plot(totalDevices2[:2], totalTimeForRegistration5[:2], '-x')
plt.ylabel('Time (ms)')
plt.grid(True)
##########
plt.subplot(4, 2, 4)
plt.plot(totalDevices2[1:3], totalTimeForRegistration2[1:3], '-o')
plt.plot(totalDevices2[1:3], totalTimeForRegistration3[1:3], '-v')
plt.plot(totalDevices2[1:3], totalTimeForRegistration4[1:3], '-s')
plt.plot(totalDevices2[1:3], totalTimeForRegistration5[1:3], '-x')
plt.grid(True)
##########
plt.subplot(4, 2, 5)
plt.plot(totalDevices2[2:4], totalTimeForRegistration2[2:4], '-o')
plt.plot(totalDevices2[2:4], totalTimeForRegistration3[2:4], '-v')
plt.plot(totalDevices2[2:4], totalTimeForRegistration4[2:4], '-s')
plt.plot(totalDevices2[2:4], totalTimeForRegistration5[2:4], '-x')
plt.ylabel('Time (ms)')
plt.grid(True)
##########
plt.subplot(4, 2, 6)
plt.plot(totalDevices2[3:5], totalTimeForRegistration2[3:5], '-o')
plt.plot(totalDevices2[3:5], totalTimeForRegistration3[3:5], '-v')
plt.plot(totalDevices2[3:5], totalTimeForRegistration4[3:5], '-s')
plt.plot(totalDevices2[3:5], totalTimeForRegistration5[3:5], '-x')
plt.grid(True)
##########
plt.subplot(4, 2, 7)
plt.plot(totalDevices2[4:6], totalTimeForRegistration2[4:6], '-o')
plt.plot(totalDevices2[4:6], totalTimeForRegistration3[4:6], '-v')
plt.plot(totalDevices2[4:6], totalTimeForRegistration4[4:6], '-s')
plt.plot(totalDevices2[4:6], totalTimeForRegistration5[4:6], '-x')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.ylabel('Time (ms)')
plt.grid(True)
##########
plt.subplot(4, 2, 8)
plt.plot(totalDevices2[5:], totalTimeForRegistration2[5:], '-o')
plt.plot(totalDevices2[5:], totalTimeForRegistration3[5:], '-v')
plt.plot(totalDevices2[5:], totalTimeForRegistration4[5:], '-s')
plt.plot(totalDevices2[5:], totalTimeForRegistration5[5:], '-x')
plt.xlabel('Total devices attempting to obtain resources from the network')
plt.grid(True)
plt.savefig('graphs/time_framework.png')
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
plt.title('Total resources offered for downlink (Subcarriers) - 700 devices')
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
plt.title('Total resources offered for uplink (Subcarriers) - 700 devices')
plt.xlabel('Number of subcarriers/Number of symbols')
plt.ylabel('Number of subcarriers offered')
plt.legend(loc='upper center', shadow=True)
plt.grid(True)
plt.savefig('graphs/resources_uplink_100_700_devices.png')
plt.show()
##########
'''