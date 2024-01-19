#version 0.2.1

import nuke

nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./images')

print("Loading Visual Magic Toolkit")

#setup menu
toolbar = nuke.toolbar('Nodes')
vmNode = toolbar.addMenu('Visual Magic', icon = 'vmlogo.png')

#add gizmos
vmNode.addCommand('AOVEdit', 'nuke.createNode(\"AOVEdit\")')
vmNode.addCommand('Despeckle', 'nuke.createNode(\"Despeckle\")')
vmNode.addCommand('DotGrid', 'nuke.createNode(\"DotGrid\")')
vmNode.addCommand('NoiseBegone', 'nuke.createNode(\"Noise_Begone\")')
vmNode.addCommand('NormalLight', 'nuke.createNode(\"NormalLight\")')
vmNode.addCommand('Toaster', 'nuke.createNode(\"Toaster\")')

print("Visual Magic Toolkit Successfully Loaded")
