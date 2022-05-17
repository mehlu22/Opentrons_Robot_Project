#!/usr/bin/env python
# coding: utf-8

# In[19]:


from opentrons import protocol_api

import opentrons.execute

#metadata
metadata = {
    'protocolName': 'Test magnetic module with magnetic beads in PCR plate',
    'author': 'Mehlam Saifudeen <mehlu22@gmail.com',
    'description': 'Test magnetic module with magnetic beads in PCR plate',
    'apiLevel': '2.12'
}

protocol = opentrons.execute.get_protocol_api('2.12')

#Homing the robot
protocol.home()

# This file has all the updated labware loaded into the robot on the correct slots
# Insert temperature and magnetic modules

temp_module = protocol.load_module('temperature module gen2', '10')
magnetic_module = protocol.load_module('Magnetic Module GEN2', '7')


#Load labware in the slots
temperature_plate = temp_module.load_labware('opentrons_24_aluminumblock_nest_2ml_snapcap')
magnetic_plate = magnetic_module.load_labware('biorad_96_wellplate_200ul_pcr')
eppendorf_plate = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', '1')
reservoir = protocol.load_labware('nest_12_reservoir_15ml', '3')
reservoir2 = protocol.load_labware('nest_12_reservoir_15ml', '6')
tiprack_1_1000ul = protocol.load_labware('opentrons_96_filtertiprack_1000ul', '4')
tiprack_2_1000ul = protocol.load_labware ('opentrons_96_filtertiprack_1000ul', '11')
tiprack_3_20ul = protocol.load_labware('opentrons_96_filtertiprack_20ul', '5')
pcr_plate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '9')
well_plate_1 = protocol.load_labware('nest_96_wellplate_200ul_flat', '2')
well_plate_2 = protocol.load_labware('corning_24_wellplate_3.4ml_flat', '8')

# Pipettes
p1000 = protocol.load_instrument('p1000_single_gen2','left', tip_racks=[tiprack_1_1000ul, tiprack_2_1000ul])
p20 = protocol.load_instrument('p20_single_gen2','right', tip_racks=[tiprack_3_20ul])

# Run the protocol
p1000.pick_up_tip(tiprack_1_1000ul['A1'])
p1000.well_bottom_clearance.dispense = '8'
p1000.mix(8, 80, eppendorf_plate['B1'], rate = 0.1)
p1000.aspirate(70, eppendorf_plate['B1'], 0.1)
p1000.dispense(35, magnetic_plate['D12'], 0.1)
p1000.dispense(35, magnetic_plate['E12'], 0.1)
#p1000.dispense(20, magnetic_plate['E12'], 0.1)
#p1000.dispense(20, magnetic_plate['F12'], 0.1)
#p1000.dispense(20, magnetic_plate['G12'], 0.1)
p1000.blow_out()
p1000.drop_tip()
p1000.pick_up_tip(tiprack_1_1000ul['A2'])
p1000.well_bottom_clearance.aspirate = '5'
p1000.well_bottom_clearance.dispense = '10'
p1000.aspirate(200, eppendorf_plate['A1'], 0.1)
p1000.dispense(100, magnetic_plate['D12'], 0.1)
p1000.dispense(100, magnetic_plate['E12'], 0.1)
#p1000.dispense(100, magnetic_plate['E12'], 0.1)
#p1000.dispense(100, magnetic_plate['F12'], 0.1)
#p1000.dispense(100, magnetic_plate['G12'], 0.1)
p1000.blow_out()
p1000.drop_tip()

#Starting the magnetic module to see if the beads are attracted to the magnet
magnetic_module.disengage()
magnetic_module.engage(height = 11.5)
print(magnetic_module.status)


#Print the entire protocol in the UI
for line in protocol.commands():
    print(line)




# In[15]:


magnetic_module.disengage()
magnetic_module.engage(height = 12)
print(magnetic_module.status)


# In[16]:


magnetic_module.disengage()


# In[ ]:




