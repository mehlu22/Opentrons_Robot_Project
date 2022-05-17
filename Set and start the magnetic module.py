#!/usr/bin/env python
# coding: utf-8

# In[3]:


from opentrons import protocol_api

metadata = {'apiLevel': '2.12'}


# Import opentrons.execute

import opentrons.execute


# This is where you establish the API version 

protocol = opentrons.execute.get_protocol_api('2.12')


# Must home before running 

# protocol.home()


# Labware

magnetic_module = protocol.load_module('Magnetic Module GEN2', '7')
plate = magnetic_module.load_labware('corning_24_wellplate_3.4ml_flat')
magnetic_module.disengage()
magnetic_module.engage(height = 11.5)
print(magnetic_module.status)




# Read protocol
for line in protocol.commands():
    print(line)


# In[ ]:





# In[ ]:




