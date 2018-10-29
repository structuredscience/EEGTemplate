"""Template script for running EEG preprocessing.

Moving from notebook -> script

1) Generalize, in the notebook, load file procedure
    - Have data all in one folder, in the notebook scan the folder, get a list of all files
    - Filter files: files = [file_name for file_name in subj_files if 'FILE_TYPE' in file_name]
"""

## IMPORTS
import os
from os.path import join as pjoin

import mne
from mne.preprocessing import ICA, read_ica
from autoreject import AutoReject

###################################################################################################
###################################################################################################

# SETTINGS

#  Anything that is a predefined parameter or setting, to be used across all subjects
#    Anything that we might change
#    Purpose: everything in one place

# Note: Settings are defined as globals
#  This makes them accessible from within the 'main' function

# Processing options
RUN_ICA = False
RUN_AUTOREJECT = False

# Set paths for the project
BASE_PATH = "path/to/project/directory"
DATA_PATH = op.join(SAVE_PATH, "Data")
ANALYSIS_PATH = op.join(SAVE_PATH, "Analysis")
RESULTS_PATH = op.join(ANALYSIS_PATH, "Results")
ICA_PATH = op.join(ANALYSIS_PATH, "ICA")
REJ_PATH = op.join(ANALYSIS_PATH, "REJ")

# Set event codes
_ADD_EVENT_RELATED_STUFF_HERE_ = None

# Set channel groups
EOG_CHS = []

# Set other settings
MY_VAR = 'value'

###################################################################################################
###################################################################################################

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


        ## DATA LOADING & SET UP ##

        # Load subject of data
        eeg_dat = '' # mne.io.read_...

        # Set any channel types - if needed

        # Load / set up montage
        chs = mne.channels.read_montage(_STANDARD_MONTAGE_NAME_, eeg.ch_names)
        eeg_dat.set_montage(chs)

        # Do any event management needed
        evs = eeg_dat.find_events(eeg_dat)  # Get the array of events - if needed

        # Set EEG reference if needed
        #   Note: depending on what you're referencing to, might want to do this later
        eeg_dat.set_eeg_reference(_REFERENCE_TO_SET_)

        ## EPOCHING ##

        # Epoch data
        epochs = mne.Epochs(eeg_dat, evs, ev_dict, tmin, tmax,
                            baseline=None, preload=True, verbose=False)

        ## RUN ICA ##

        if RUN_ICA:

            print('\tRunning ICA')

            # ICA Settings: NOTE - UPDATE THESE AS NEEDED
            method = 'fastica'
            n_components = 0.99
            random_state = 47
            reject = {'eeg': 20e-4}
            thresh = 2.5

            # Initialize ICA object
            ica = ICA(n_components=n_components, method=method, random_state=random_state)

            # High-pass filter data for running ICA
            eeg_dat.filter(l_freq=1., h_freq=None, fir_design='firwin');

            # Fit ICA
            ica.fit(eeg_dat, reject=reject)

            # Find components to drop, based on correlation with EOG channels
            drop_inds = []
            for chi in EOG_CHS:
                inds, scores = ica.find_bads_eog(eeg_dat, ch_name=chi,
                                                 threshold=thresh, verbose=False)
                drop_inds.extend(inds)
            drop_inds = list(set(drop_inds))

            # Set which components to drop, and collect record of this
            ica.exclude = drop_inds
            #dropped_components[s_ind, 0:len(drop_inds)] = drop_inds

            # Save out ICA solution
            ica.save(pjoin(ICA_PATH, str(subj_ind) + '-ica.fif'))

            # Apply ICA to data
            eeg_dat = ica.apply(eeg_dat);

        ## RUN AUTOREJECT ##

        if RUN_AUTOREJECT:

            print('\tRunning AutoReject')

            # Initialize and fit autoreject model across epochs
            ar = AutoReject(n_jobs=4, verbose=False)
            ar = ar.fit(epochs)

            # Save out autoreject - currently using a pickle file
            with open(pjoin(REJ_PATH, str(subj_ind) + '-ar.p'), 'wb') as ar_pickle_file:
                pickle.dump(ar, ar_pickle_file)

            # Apply autoreject
            # NOTE: Can apply to multiple copies of the data, here or later
            #  For example - can apply to copies that each have different filtering
            epochs, rej_log = ar.transform(epochs, return_log=True)


        ## SAVE OUT PREPROCESSED DATA ##

        # Save out preprocessed epochs object
        epochs.save(_FNAME_)
        print('\t Subject finished & saved.')


if __name__ == "__main__":
    main()
