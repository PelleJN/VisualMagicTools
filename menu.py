import nuke

#version 0.0.1

nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./images')

print("Loading Visual Magic Toolkit")

#setup menu
toolbar = nuke.toolbar('Nodes')
vmNode = toolbar.addMenu('Visual Magic', icon = 'vmlogo.png')

#add gizmos
vmNode.addCommand('AOVEdit', 'nuke.createNode(\"AOVEdit\")')
vmNode.addCommand('NoiseBegone', 'nuke.createNode(\"Noise_Begone\")')

print("Visual Magic Toolkit Successfully Loaded")
