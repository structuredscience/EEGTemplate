"""Template script for running analysis across a group of EEG subjects, after pre-processing.

Notes:
-
-

"""

###################################################################################################
###################################################################################################

## SETTINGS


###################################################################################################
###################################################################################################

def main():

    # Initialize any output variables to save out


    # Loop across all subjects
    for subj_ind, subj_file in enumerate(subj_files):


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
