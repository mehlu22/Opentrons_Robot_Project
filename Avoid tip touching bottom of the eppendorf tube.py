#!/usr/bin/env python
# coding: utf-8

# In[11]:


from opentrons import protocol_api

metadata = {'apiLevel': '2.12'}


# Import opentrons.execute

import opentrons.execute


# This is where you establish the API version 

protocol = opentrons.execute.get_protocol_api('2.11')


# Must home before running 

protocol.home()


# Labware to be loaded into the robot

plate = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', '1')
reservoir = protocol.load_labware('nest_12_reservoir_15ml', '3')
reservoir2 = protocol.load_labware('nest_12_reservoir_15ml', '6')

tiprack_1 = protocol.load_labware('opentrons_96_tiprack_1000ul','4')
tiprack_2 = protocol.load_labware('opentrons_96_tiprack_20ul', '5')

pcr_plate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '9')

# Pipette 

pipette = protocol.load_instrument('p1000_single_gen2','left', tip_racks=[tiprack_1])
pipette2 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks = [tiprack_2])


j = "ABCDEFGHI"
# Protocol steps
for k in j:
    for i in range (1,4):
        pipette.pick_up_tip(tiprack_1['{0}{1}'.format(k,i)])
        pipette.well_bottom_clearance.aspirate = '15'
        pipette.aspirate(100, plate['A{0}'.format(i)], 0.5)
        pipette.well_bottom_clearance.dispense = '15'
        pipette.dispense(100, reservoir2['A{0}'.format(i)], rate = 0.5)
        pipette.blow_out(reservoir2['A{0}'.format(i)])
        pipette.return_tip()
#pipette.transfer(150, plate['B3'], reservoir['A1'],blow_out=True, rate=5,blowout_location="destination well",new_tip="never")
#pipette.transfer(150, plate['B4'], reservoir['A2'],blow_out=True, rate=5,blowout_location="destination well",new_tip="never")
# Output steps in protocol

for line in protocol.commands():
    print(line)


# In[12]:


protocol.home()


# In[8]:


pipette.return_tip()


# In[ ]:




