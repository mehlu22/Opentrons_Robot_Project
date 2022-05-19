#!/usr/bin/env python
# coding: utf-8

# In[ ]:


ctx.set_rail_lights(True)
    ctx.delay(seconds=10)
    if sample_count < 1 or sample_count > 24:
        raise Exception('Invalid number of DNA samples (must be 1-24).')

    def pause_attention(message):
        ctx.set_rail_lights(False)
        ctx.delay(seconds=10)
        ctx.pause(message)
        ctx.set_rail_lights(True)

    pause_attention("""PCR set up: Pre-cool temp module to 4 degrees, pre-heat
    cycler block (98) and lid (105) with OT app settings, sample plate slot 1
    with up to 24 samples (in column order A1-H1), master mix tube A1 of block
    on slot 5.""")
    
    pause_attention("""Set up complete. Please transfer plate from temperature
    module to pre-heated cycler and resume to run PCR.""")
    
    pause_attention(
      """Post-PCR clean up: place beads (A1 of block in slot 5) and ethanol
      (A1 of reservoir in slot 2) on OT-2 deck.""")
    
    pause_attention("""Indexing: Place index plate (slot 1) and
    index rxn mx tube (A1 chilled block on slot 5) on OT-2 deck.""")
    
     pause_attention("""Second clean up: Place PEG NaCl (A1 of block in slot 5)
    and TE (A5 of reservoir in slot 2) on OT-2 deck. Replenish ethanol
    (A1 of reservoir in slot 2).""")
        
    pause_attention("""Place output plate on temperature module.""")
    
    
    #The .pause() function can also be used to pause the protocol and the .resume() function can be used to resume the protocol

