# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 14:06:35 2015

@author: Andrew Erskine
"""

from PyDAQmx import Task
from numpy import zeros

"""This example is a PyDAQmx version of the ContAcq_IntClk.c example
It illustrates the use of callback functions

This example demonstrates how to acquire a continuous amount of
data using the DAQ device's internal clock. It incrementally stores the data
in a Python list.
"""

# class CallbackTask(Task):
#     def __init__(self):
#         Task.__init__(self)
#         self.data = zeros(1000)
#         self.a = []
#         self.CreateAIVoltageChan("cDAQ1Mod3/ai0","",DAQmx_Val_Cfg_Default,-10.0,10.0,DAQmx_Val_Volts,None)
#         self.CfgSampClkTiming("",10000.0,DAQmx_Val_Rising,DAQmx_Val_ContSamps,1000)
#         self.AutoRegisterEveryNSamplesEvent(DAQmx_Val_Acquired_Into_Buffer,1000,0)
#         self.AutoRegisterDoneEvent(0)
#     def EveryNCallback(self):
#         read = int32()
#         self.ReadAnalogF64(1000,10.0,DAQmx_Val_GroupByScanNumber,self.data,1000,byref(read),None)
#         self.a.extend(self.data.tolist())
#         print self.data[0]
#         return 0 # The function should return an integer
#     def DoneCallback(self, status):
#         print "Status",status.value
#         return 0 # The function should return an integer
#
#
# task=CallbackTask()
# task.StartTask()
#
# raw_input('Acquiring samples continuously. Press Enter to interrupt\n')
#
# task.StopTask()
# task.ClearTask()

task = DoAiMultiTaskCallback("Mod2/ai3", "", "Mod1/port0/line0", 10000.0, 6.0, numpy.zeros((2, 1000)), "/cDaQ/ai/SampleClock", 0.1, 2)
task.StartThisTask()