import os
import shutil
import zipfile
import glob
import operator

file_list = []  # Define the file_list variable
infilecounter = 0  # Define the infilecounter variable
outfilecounter = 0  # Define the outfilecounter variable
source_directory = ""  # Define the source_directory variable
local_path = ""  # Define the local_path variable

for compressed_file in file_list[infilecounter:]:
    # if we don't have the compressed file stored locally, go get it. Keep trying if necessary.
    while not os.path.isfile(local_path + compressed_file):
        # copy the file from the source directory to the local directory
        shutil.copy(source_directory + compressed_file, local_path)
        
        # extract the compressed file
        z = zipfile.ZipFile(file=local_path + compressed_file, mode='r')
        z.extractall(path=local_path + 'tmp/')
        
        # parse each of the csv files in the working directory
        for infile_name in glob.glob(local_path + 'tmp/*'):
            outfile_name = local_path + 'tmp/' + os.path.basename(infile_name)
            
            # open the infile and outfile
            with open(infile_name, mode='r') as infile, open(outfile_name, mode='w') as outfile:
                for line in infile:
                    # extract lines with our interest country code
                    if #
                outfilecounter += 1
                
                # delete the temporary file
                os.remove(infile_name)
                
            infilecounter += 1
    
    print('done')
