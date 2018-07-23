"""

Moving from notebook -> script

1) Generalize, in the notebook, load file procedure
    - Have data all in one folder, in the notebook scan the folder, get a list of all files
    - Filter files: files = [file_name for file_name in subj_files if '.mat' in file_name]
"""

## IMPORTS
import mne

##
##

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
DAT_PATH = '/Users/tom/Documents/Research/1-Projects/Phase/Experiments/rtPB/2-Data/rtPB-3/processed/EEG/'

# Set other settings
MY_VAR = 'value'


##
##

# Running through the subjects
#  Everything from load & after - in a loop


def main():
    """   """

    # SETUP
    # Any work that's outside the loop

    # Get all subj files (clean the list if needed)
    subj_files = []

    # Set up any group level collections
    outputs = np.array(shape=[10, 10])

    # Loop across all subjects
    for subj_ind, subj_file in enumerate(subj_files):
        pass

        # Add status updates
        print('Running Subject # ', subj_ind)

        # Load subject of data

        # Do a pre-processing

        # Do analyses of interest

        # Note: might have to add try/excepts for problems
        try:
            pass
        except:
            print('Subject number' subj_ind, 'failed.')

        # Note: remember to collect things of interest into group stores
        #  and/or save out individual files (however makes sense)

    # Save any group level files
    np.save(outputs, 'check')


if __name__ == "__main__":
    main()
