#!/usr/bin/env python
# coding: utf-8

# In[8]:


from opentrons import protocol_api
import threading
import time

metadata = {
    'apiLevel': '2.11'
}

import opentrons.execute

protocol = opentrons.execute.get_protocol_api('2.11')


while True:
    protocol.set_rail_lights(True)
    time.sleep(1)
    protocol.set_rail_lights(False)
    time.sleep(1)
    

tip_rack = protocol.load_labware('opentrons_96_tiprack_300ul', 8)
pipette = protocol.load_instrument('p300_multi_gen2', 'left')
    
if not protocol.is_simulating():
    thread = threading.Thread(target=flash_lights_infinitely, args=(protocol,))
    thread.start()
    
pipette.pick_up_tip(tip_rack.wells()[0])
pipette.drop_tip(tip_rack.wells()[0])
protocol.delay(minutes=5)
pipette.pick_up_tip(tip_rack.wells()[0])
pipette.drop_tip(tip_rack.wells()[0])
    
  



# In[ ]:




