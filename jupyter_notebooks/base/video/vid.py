import pynq
from pynq import Overlay
from pynq.lib.video import *

base = Overlay('base.bit')
hdmi_in = base.video.hdmi_in
hdmi_out = base.video.hdmi_out


async def readframes():
    while True:
        frame = await hdmi_in.readframe_async()
        dma.sendchannel.transfer(frame)
        await dma.sendchannel.wait_async()
        frame.freebuffer()

async def writeframes():
    while True:
        frame = hdmi_out.new_frame()
        dma.recvchannel.transfer(frame)
        await dma.recvchannel.transfer(frame)
        await hdmi_out.writeframe_aysnc(frame)

