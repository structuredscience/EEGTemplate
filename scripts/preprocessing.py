"""Template script for running EEG preprocessing.

Moving from notebook -> script

1) Generalize, in the notebook, load file procedure
    - Have data all in one folder, in the notebook scan the folder, get a list of all files
    - Filter files: files = [file_name for file_name in subj_files if '.mat' in file_name]
"""

## IMPORTS
import mne

from mne.preprocessing import ICA, read_ica
from autoreject import AutoReject

###################################################################################################
###################################################################################################

# SETTINGS

#  Anything that is chosen variable, across all subjects
#    Anything that we might change
#    Purpose: everything in one place

# Note: Settings are defined as globals
#  This makes them accessible from within the 'main' function

# Processing options
RUN_ICA = False
RUN_AUTOREJECT = False

# Set data path
DATA_PATH = 'path/to/data/files'

# Set other settings
MY_VAR = 'value'

###################################################################################################
###################################################################################################

# Running through the subjects
#  Everything from load & after - in a loop

def main():

    # SETUP
    # Any work that's outside the loop

    # Get all subj files
    #   This also set up to do some kind of cleaning of the files list, list if needed
    subj_files = [file_name for file_name in os.listdir(DATA_PATH) if 'FILE_TYPE' in filename]
    n_subjs = len(subj_files)

    # Set up any group level collections
    outputs = np.array(shape=[10, 10])

    # Loop across all subjects
    for subj_ind, subj_file in enumerate(subj_files):

        # Add status updates
        print('Running Subject # ', subj_ind)

        # Load subject of data


        # Do a pre-processing








if __name__ == "__main__":
    main()
