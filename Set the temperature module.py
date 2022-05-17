#!/usr/bin/env python
# coding: utf-8

# In[1]:


from opentrons import protocol_api

metadata = {'apiLevel': '2.12'}


# Import opentrons.execute

import opentrons.execute


# This is where you establish the API version 

protocol = opentrons.execute.get_protocol_api('2.12')


# Must home before running 

#protocol.home()


# Labware

temp_module = protocol.load_module('temperature module gen2', '10')
plate = temp_module.load_labware('opentrons_24_aluminumblock_nest_2ml_snapcap')
temp_module.set_temperature(20)
print(temp_module.temperature)
print(temp_module.status)
print(temp_module.target)
temp_module.deactivate()


# Read protocol
for line in protocol.commands():
    print(line)


# In[2]:


temp_module.deactivate()


# In[ ]:


temp

