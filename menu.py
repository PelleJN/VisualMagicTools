#version 0.3.0

import nuke

nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./images')
nuke.pluginAddPath('./python')

print("Loading Visual Magic Toolkit")

nuke.load('BKR_Main')

#setup menu
toolbar = nuke.toolbar('Nodes')
vmNode = toolbar.addMenu('Visual Magic', icon = 'vmlogo.png')

#add gizmos
vmNode.addCommand('AOVEdit', 'nuke.createNode(\"AOVEdit\")', icon="aovedit.png")
vmNode.addCommand('ColorToColor', 'nuke.createNode(\"ColorToColor\")', icon="colortocolor.png")
vmNode.addCommand('Despeckle', 'nuke.createNode(\"Despeckle\")', icon="despeckle.png")
vmNode.addCommand('DotGrid', 'nuke.createNode(\"DotGrid\")')
vmNode.addCommand('NoiseBegone', 'nuke.createNode(\"Noise_Begone\")')
vmNode.addCommand('NormalLight', 'nuke.createNode(\"NormalLight\")', icon="normallight.png")
vmNode.addCommand('NukeBake', 'nuke.createNode("NukeBake") if nuke.script_directory() and nuke.script_directory() != "" else nuke.message("Please save your script before trying to use NukeBake!")', icon="nukebake.png") #Only add if script is saved.
vmNode.addCommand('Toaster', 'nuke.createNode(\"Toaster\")')

print("Visual Magic Toolkit Successfully Loaded")

