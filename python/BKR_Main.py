import os
from BKR_NamesAndColors import *
from BKR_Modules import *



#################
### FUNCTIONS ###
#################


# GENERATE PAIR
def bkr_main_generate_pair():
    """
    Generates a pair of an avaliable Name and Color.

    Returns:
    - NAME_COLOR string
    """
    
    scriptDir = nuke.script_directory()
    scriptDirName = nuke.scriptName()
    scriptName = os.path.splitext(os.path.basename(scriptDirName))[0]
    pathToRenders = scriptDir+"/nukebake/"+scriptName

    bkr_possible_names = bkr_generate_possible_names_dict(bkr_names_list, bkr_colors_list)
    
    if os.path.exists(pathToRenders): # If path is valid
        subtractdict = bkr_create_name_color_dict(bkr_filter_names_colors(bkr_get_folder_names(pathToRenders), bkr_names_list, bkr_colors_list))
    else:
        subtractdict = {} 

    valid_names_dict = bkr_remove_dict_values(bkr_possible_names, subtractdict)
    
    return bkr_generate_name_color_pair(valid_names_dict)