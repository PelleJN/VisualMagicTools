import os
import re
import random



#########################
### FILES AND FILTERS ###
#########################



def bkr_get_folder_names(directory_path):
    """
    Get a list of every folder in a directory

    Args:
    - directory_path: The directory to search

    Returns:
    - folders: A list of the folders.
    """
    # Get all items (files and folders) in the specified directory
    items = os.listdir(directory_path)

    # Filter out only the folders
    folders = [item for item in items if os.path.isdir(os.path.join(directory_path, item))]

    return folders



def bkr_filter_names_colors(folders_list, names_list, colors_list):
    """
    Removes all list entries that don't match allowed NAME_COLOR combinations. 

    Parameters:
    - folders_list: List of entries being filtered
    - names_list: List of valid names
    - colors_list: List of valid colors

    Returns:
    - Updated list (filtered_list)
    """
    filtered_list = []

    for item in folders_list:
        # Split the item into two parts using '_' as a separator
        parts = item.split('_')

        # Check if the item has exactly two parts
        if len(parts) == 2:
            # Convert both parts to uppercase
            name_part = parts[0].upper()
            color_part = parts[1].upper()

            # Check if both parts match the criteria
            if name_part in map(str.upper, names_list) and color_part in map(str.upper, colors_list):
                # If both match, add the original item to the filtered list
                filtered_list.append(item)

    return filtered_list



def bkr_find_used_bakes(base_dir, folder_names, scriptName):
    """
    Returns all folders in a directory that contain a file matching a valid bake format. 

    Parameters:
    - base_dir: The directory to check in
    - folder_names: The list of names to check
    - scriptName: The name of the script, used for checking the file name.

    Returns:
    - used_bakes_list (list)
    """
    used_bakes_list = []  # List to store folders that match the criteria

    # Iterate through each folder name provided
    for folder_name in folder_names:
        folder_path = os.path.join(base_dir, folder_name)  # Get full path of the folder
        if os.path.isdir(folder_path):  # Check if the path is a directory
            # Iterate through files in the folder
            for filename in os.listdir(folder_path):
                # Check if the filename matches the specified pattern
                if filename.startswith(f"nukebake_{scriptName}_{folder_name}_v"):
                    if re.match(r'nukebake_[\w]+_[\w]+_v\d+_\d+\.exr', filename): # See explanation below because god knows I need it
                        # If a matching file is found, add the folder to the list
                        used_bakes_list.append(folder_name)
                        break  # Once a matching file is found, no need to continue checking the rest of the files
    return used_bakes_list  # Return the list of matching folders

    # Regex explanation:

    # 'nukebake_': This part matches the literal string "nukebake_".
    # '[\w]+': This matches one or more word characters. \w matches any alphanumeric character and underscores.
    # '_': This matches the literal underscore character.
    # '[\w]+': Again, matches one or more word characters.
    # '_v': This matches the literal string "_v".
    # '\d+': This matches one or more digits.
    # '_': This matches another underscore.
    # '\d+': This again matches one or more digits.
    # '\.exr': This matches the literal string ".exr".

    # Putting it all together, the regular expression matches strings that follow this pattern:

    # nukebake_[VariableName]_[FolderName]_v###_####.exr



def bkr_split_by_last_char(input_string, character):
    """
    Split the input string at the last occurrence of the specified character
    and return both halves.

    Args:
    - input_string (str): The string to be split.
    - character (str): The character at which to split the string.

    Returns:
    - Tuple containing two strings: The first half of the input string
    before the last occurrence of the specified character and the second
    half starting from the last occurrence of the character.
    """
    last_occurrence_index = input_string.rfind(character)
    if last_occurrence_index == -1:
        # If the character is not found, return the entire string and an empty string
        return input_string, ""
    else:
        # Split the string at the last occurrence of the character
        first_half = input_string[:last_occurrence_index]
        second_half = input_string[last_occurrence_index + 1:]
        return first_half, second_half



def bkr_check_for_file(file_path, match_last="_"):
    """
    Check if a file exists at the specified path.

    Parameters:
    - file_path: The path of the file to check for existence.
    - match_last: If anything, returns true even if the file path only matches up until the last instance of this character. Useful for excluding file endings. Defaults to underscore.

    Returns:
    - True if the file exists, False otherwise.
    """
    if match_last and match_last != "":
        # Extract the base name of the file
        file_path_base = os.path.basename(file_path)
        file_path_prefix = bkr_split_by_last_char(file_path_base, match_last)[0]
        
        # Iterate over files in the directory of the file path
        for root, dirs, files in os.walk(os.path.dirname(file_path)):
            for file in files:
                # Check if any file starts with the extracted prefix
                if file.startswith(file_path_prefix):
                    return True
        # If no matching file is found, return False
        return False
    else:
        # Check if the file exists using os.path.isfile
        return os.path.isfile(file_path)
    


def bkr_find_min_max_frame_number(folder_path):
    """
    Finds the smallest and largest frame numbers among the EXR files in the given folder path.

    Parameters:
    - folder_path (str): The path to the folder containing the EXR files.

    Returns:
    - min_frame (int): The smallest frame number found.
    - max_frame (int): The largest frame number found.
    """
    # Check if the provided path is a directory
    if not os.path.isdir(folder_path):
        raise ValueError("The provided path is not a directory.")
    
    # List all files in the directory
    files = os.listdir(folder_path)
    frame_numbers = []
    
    # Iterate through each file in the directory
    for file_name in files:
        # Check if the file is an EXR file
        if file_name.endswith('.exr'):
            # Split the file name by underscores to extract the frame number
            parts = file_name.split('_')
            last_part = parts[-1]
            # Extract the frame number and convert it to an integer
            frame_number = int(last_part.split('.')[0])
            # Add the frame number to the list
            frame_numbers.append(frame_number)
    
    # Check if there are any EXR files in the directory
    if not frame_numbers:
        raise ValueError("No EXR files found in the directory.")
    
    # Find the smallest and largest frame numbers
    min_frame = min(frame_numbers)
    max_frame = max(frame_numbers)
    
    return min_frame, max_frame



def bkr_get_folder_size(folder_path):
    """
    Returns the size of the specified folder in megabytes.

    Args:
    - folder_path: The folder to look at

    Returns:
    - total_size_mb: The size of everything in the folder, in MB.
    """
    total_size_mb = 0

    # Walk through all the directories and files within the folder
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            # Calculate the size of each file in megabytes and add it to the total size
            total_size_mb += os.path.getsize(file_path) / (1024 * 1024)

    return total_size_mb



#####################
### DATA MANAGERS ###
#####################



def bkr_create_name_color_dict(data_list):
    """
    Create a dictionary where the key is the name and the value is a list of colors.

    Args:
    - data_list (list): A list of strings in the format 'Name_Color'.

    Returns:
    - dict: A dictionary with names as keys and lists of colors as values.
    """
    name_color_dict = {}

    # Iterate through each entry in the data list
    for entry in data_list:
        # Split the entry into name and color
        name, color = entry.split('_')

        # Check if the name is already in the dictionary
        if name in name_color_dict:
            # If yes, append the color to the existing list
            name_color_dict[name].append(color)
        else:
            # If no, create a new list with the color
            name_color_dict[name] = [color]

    return name_color_dict



def bkr_generate_possible_names_dict(names_list, colors_list):
    data_dict = {name: colors_list for name in names_list}
    return data_dict



def bkr_remove_dict_values(basedict, subtractdict):
    """
    Remove values from basedict based on subtractdict.

    Parameters:
    - basedict: First dictionary
    - subtractdict: Second dictionary

    Returns:
    - Updated dictionary (basedict)
    """
    for key in subtractdict:
        if key in basedict:
            basedict[key] = [value for value in basedict[key] if value not in subtractdict[key]]
    
    return basedict



def bkr_generate_name_color_pair(valid_names_dict):

    data = valid_names_dict

    # Choose a random key
    random_key = random.choice(list(data.keys()))

    # Choose a random value from the selected key's list
    random_value = random.choice(data[random_key])

    # Combine them into a string
    result_string = f"{random_key}_{random_value}"

    return result_string

