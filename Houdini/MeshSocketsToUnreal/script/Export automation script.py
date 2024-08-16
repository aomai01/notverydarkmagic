# The following script emulates the manual process of repreatedly
# going to File > Export > Filmbox FBX... to export different FBX files with sockets.


# 1. Do the following only once (manually or using a Python SOP)

# Creates a reusable node bundle. You can name it whatever.
# The node bundles are saved to the HIP file.
hou.addNodeBundle('object_with_sockets')

# Creates a reusable ROP to export every FBX file
rop = hou.node('/out').createNode('filmboxfbx')

# Sets the Export parameter of the ROP to the name of the node bundle, starting with a '@'
rop.parm('startnode').set('@object_with_sockets')


# 2. Do the following per FBX file (probably using a Python SOP in a loop)

# Gets an existing node bundle by its name
bundle = hou.nodeBundle('object_with_sockets')

# Sets this bundle's pattern to the paths of the OBJ nodes you need to export, separated by single spaces.
# The example file "Static Mesh Sockets.hip" is already set up in a way that for every recook (i.e. every unique asset), 
# the Python SOP will delete and recreate the Subnetwork OBJ /obj/sockets, so the "/obj/sockets" part of the pattern string
# will remain the same every time. The first part of the pattern string, "/obj/capy", may vary per FBX file.
bundle.setPattern('/obj/capy /obj/sockets')

# Sets the Output File parameter of the ROP to the path unique to this FBX file
rop.parm('sopoutput').set('$HIP/export/capy.fbx')

# Exports the FBX file
rop.render()
