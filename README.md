# Dotfiles

My personal dot and config files. Includes things from bashrc to colorschemes to syntax files
The intention is to be able to quickly get my dotfiles on any linux system

## mklink.py

The script that puts the files in place.
'./mklink.py linkfile.txt'
linkfile.txt is a csv file with the following format:
* Column 1: file name (located in configs directory)
* Column 2: path to where the file should be linked
* Column 3: prefix to file name (generally "." or nothing at all)

mklink.py will try to create the path if it doesn't exist, then symlink the file to that path  

Files can then be modified from the `config` directory and will be updated automatically (with the exception of files that need to be sourced)
