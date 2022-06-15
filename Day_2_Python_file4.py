#!/usr/bin/env python
# coding: utf-8

# In[1]:


from opentrons import protocol_api
from opentrons.protocol_api.labware import Well, OutOfTipsError, TipSelectionError
from types import MethodType
from opentrons import types
import pandas as pd

# Import opentrons.execute

import opentrons.execute


# This is where you establish the API version 

protocol = opentrons.execute.get_protocol_api('2.12')


#metadata
metadata = {
    'protocolName': "3' mRNA Next Gen Sequencing Protocol File 4",
    'author': 'Mehlam M Saifudeen <mehlu22@gmail.com>',
    'description': 'Endpoint PCR',
    'apiLevel': '2.12'
}

def run(protocol):
    #Input the required number of experiments to be run
    num_of_experiments = int(input("Please enter the number of experiments you would like to run: \n"))
    copy = copy_2 = copy_3 = copy_4 = num_of_experiments
    
    # Must home before running
    protocol.home()

#     [uploaded_csv, num_samples, num_of_experiments, num_of_tips_1, num_of_tips_2, num_of_tips_3, num_of_tips_4, asp_rate, disp_rate] 
#     = get_values('uploaded_csv', 'num_samples', 'num_of_experiments', 'num_of_tips_1', 'num_of_tips_2', 'num_of_tips_3', 'num_of_tips_4', 'asp_rate', 'disp_rate')
    
    #Turn on and off the rail lights to see equiptment clearly and to test the lights
    protocol.set_rail_lights(True)
    protocol.delay(seconds = 10)
    protocol.set_rail_lights(False)
    
    #Load the temperature and the magnetic modules for the experiment
    temp_module = protocol.load_module('temperature module gen2', '7') #TODO change the position of the module as per requirements
    temp_module_2 = protocol.load_module('temperature module gen2', '10') #TODO change the position of the module as per requirements
    magnetic_module = protocol.load_module('magnetic module gen2', '9') #TODO change the position of the module as per requirements
    
    #Load the labware for the experiment into the specific positions on the robot
    temp_plate = temp_module.load_labware('opentrons_24_aluminumblock_nest_2ml_snapcap')
    temp_plate_2 = temp_module_2.load_labware('opentrons_96_aluminumblock_biorad_wellplate_200ul')
    magnetic_plate = magnetic_module.load_labware('biorad_96_wellplate_200ul_pcr')
    tuberack_1 = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical', location = '5')
    tuberack_2 = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', location = '8')
    primer_well = protocol.load_labware('nest_96_wellplate_200ul_flat', location = '6')
    tiprack_1_1000ul = protocol.load_labware('opentrons_96_filtertiprack_1000ul', '1')
    tiprack_2_1000ul = protocol.load_labware('opentrons_96_filtertiprack_1000ul', '2')
    tiprack_3_20ul = protocol.load_labware('opentrons_96_filtertiprack_20ul', '3')
    tiprack_4_20ul = protocol.load_labware('opentrons_96_filtertiprack_20ul', '4')
    
    #Load the pipettes into the tipracks
    p1000 = protocol.load_instrument('p1000_single_gen2','left', tip_racks=[tiprack_1_1000ul, tiprack_2_1000ul])
    p20 = protocol.load_instrument('p20_single_gen2','right', tip_racks=[tiprack_3_20ul, tiprack_4_20ul])
    
    #Adjusting the well bottom clearance
    p1000.well_bottom_clearance.aspirate = 4
    p1000.well_bottom_clearance.dispense = 9
    p20.well_bottom_clearance.aspirate = 9
    p20.well_bottom_clearance.dispense = 9
    
    #Adjusting the rate of aspirating and dispensing
#     p1000.flow_rate.aspirate = 100
#     p1000.flow_rate.dispense = 100
#     p20.flow_rate.aspirate = 100
#     p20.flow_rate.dispense = 100
    p1000.flow_rate.blow_out = 300
    p20.flow_rate.blow_out = 300
    
    #Parsing in the csv file into the code
    dataset = pd.read_csv('3-end_seq_scheme_051822_v1.csv', delimiter = ",", index_col = False)
    print(dataset)
    
    #Setting the temperature modules to the correct temperatures
    #temp_module_2.set_temperature(42)
    temp_module.set_temperature(24.0) #Always keep at 4 degrees C
    magnetic_module.disengage()
    
    #Prepare mastermix 4 containing PCR and E3
    p1000.pick_up_tip()
    p1000.aspirate(dataset.loc[12, 'amount-uL']*(num_of_experiments+1), temp_plate['{0}'.format(dataset.loc[12, 'slot'])], rate = 0.4)
    p1000.dispense(dataset.loc[12, 'amount-uL']*(num_of_experiments+1), temp_plate['D6'], rate = 0.4)
    p1000.blow_out(temp_plate['D6'])
    p1000.drop_tip()
    p20.pick_up_tip()
    p20.aspirate(dataset.loc[13, 'amount-uL']*(num_of_experiments+1), temp_plate['{0}'.format(dataset.loc[13, 'slot'])], rate = 0.4)
    p20.dispense(dataset.loc[13, 'amount-uL']*(num_of_experiments+1), temp_plate['D6'], rate = 0.4)
    p20.blow_out(temp_plate['D6'])
    p20.drop_tip()
    p1000.pick_up_tip()
    p1000.mix(8, 14*num_of_experiments, temp_plate['D6'], rate = 0.4)
    p1000.blow_out(temp_plate['D6'])
    p1000.drop_tip()
    
    #Adding 8ul of the mastermix to the 17.3ul of the eluted library
    rows = "ABCDEFGH"
    columns = [1,2,3,4,5,6,7,8,9,10,11,12]
    i=0
    j=-1
    while(copy!=0):
        if(j>12):
            j=0
            i+=1
        else:
            j+=1
        p20.pick_up_tip()
        p20.mix(8, 14, temp_plate['D6'], rate = 0.4)
        p20.aspirate(8, temp_plate['D6'], rate = 0.4)
        p20.dispense(8, magnetic_plate['{0}{1}'.format(rows[i], columns[j])], rate = 0.4)
        p20.blow_out(magnetic_plate['{0}{1}'.format(rows[i], columns[j])])
        p20.drop_tip()
        copy = copy - 1
        
    #Adding 5ul of the i7 primer BC
    rows = "ABCDEFGH"
    columns = [1,2,3,4,5,6,7,8,9,10,11,12]
    i=0
    j=-1
    while(copy_2!=0):
        if(j>12):
            j=0
            i+=1
        else:
            j+=1
        p20.pick_up_tip()
        p20.mix(5, 5, primer_well['{0}{1}'.format(rows[i], columns[j])], rate = 0.4)
        p20.aspirate(5, primer_well['{0}{1}'.format(rows[i], columns[j])], rate = 0.4)
        p20.dispense(5, magnetic_plate['{0}{1}'.format(rows[i], columns[j])], rate = 0.4)
        p20.mix(8, 5, magnetic_plate['{0}{1}'.format(rows[i], columns[j])], rate = 0.4)
        p20.blow_out(magnetic_plate['{0}{1}'.format(rows[i], columns[j])])
        p20.drop_tip()
        copy_2 = copy_2 - 1
        
        #Home the protocol
        protocol.home()
        protocol.pause('This is the end of the fourth part of the protocol')
        #temp_module.deactivate()
        #temp_module_2.deactivate()
        
        # Output steps in protocol
        for line in protocol.commands():
            print(line)

#Running the protocol
run(protocol)


# In[ ]:


protocol.home()


# In[ ]:




