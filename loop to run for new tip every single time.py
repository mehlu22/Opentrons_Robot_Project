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


# Labware 

plate = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', '1')
reservoir = protocol.load_labware('nest_12_reservoir_15ml', '3')
reservoir2 = protocol.load_labware('nest_12_reservoir_15ml', '6')

tiprack_1 = protocol.load_labware('opentrons_96_tiprack_1000ul',location = '4')
pcr_plate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '9')


# Pipette 

p1000 = protocol.load_instrument('p1000_single_gen2','left', tip_racks=[tiprack_1])
n = 1
j = "ABCDEFGHI"
# Protocol steps
for k in j:
    for i in range (1,13):
        p1000.pick_up_tip(tiprack_1['{0}{1}'.format(k,i)])
        p1000.aspirate(25, plate['A2'], rate = 0.5)
        p1000.dispense(25, reservoir['A{0}'.format(i)], rate = 0.5)
        p1000.blow_out(reservoir['A{0}'.format(i)])
        p1000.return_tip()
#p1000.transfer(150, plate['B3'], reservoir['A1'],blow_out=True, rate=5,blowout_location="destination well",new_tip="never")
#p1000.transfer(150, plate['B4'], reservoir['A2'],blow_out=True, rate=5,blowout_location="destination well",new_tip="never")
# Output steps in protocol

for line in protocol.commands():
    print(line)


# In[10]:


protocol.home()


# In[9]:


p1000.drop_tip()


# In[ ]:




