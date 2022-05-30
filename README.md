# AFMTool
AFM Tool for automating data analysis for  .spm files

## Functionailites
- Generate 2D, 3D plot
- Generate roughness(RA) for Cu and polymer 
- Generate step height
- Generate roll-off
- Automatically generate Excel sheet containing above values

## Installation 
- Download the entire AFMTOOL folder onto Desktop. If you're downloading from Github, click the green `Code` button on top of the list of files, and click `Download Zip`. Move the downloaded folder onto your Desktop
- You need to have Python version>=3.9 to run the script. 
- Check if Python is installed in your computer:
    - Open command line. In Windows, press Windows logo + S to launch search window, and search `cmd`. 
    - In command line, type: `python --version`
    - If Python has been installed, the version that is in your computer will be returned. 
![Check python ver](https://user-images.githubusercontent.com/105037297/169487975-c7da6c6f-da46-44d2-bda3-5d8dd35987d7.PNG)
    - If an error message is returned, Python has not been installed. You can download it here: https://www.python.org/downloads/
- If Python has been installed in your computer, you need to proceed to install the required Python libraries that is needed to run the script. In the command line, type `cd %HOMEPATH%/Desktop/AFMTOOL` and press Enter. After that, type `pip install -r requirements.txt` and wait for installation to be completed.
- If no error messages appeared on the terminal, you have successfully installed the packages needed to run the script, please refer to Usage section below on how to run the script. 

## Usage

1. Open Windows command line (press Windows logo + S to launch search window, and search `cmd`)
2. Type into command line:  `cd %HOMEPATH%/Desktop/AFMTOOL/AFMTOOL` and press Enter
3. Type into command line: `python3 AFMtool.py` and press Enter. (Shortcut: enter `python3 a` then press Tab for autofill)
4. File Explorer window pops up. Drag and select files to be analyzed, and click `Open`. 
5. Scripts starts to process files. You can see in the progress bar in the terminal line how many files it has processed. Time needed is approximately 10s per file. 
6. If you want to terminate the process halfway, press CTRL+C. 
7. After all scripts has been processed, you can find the Excel file generated by clicking into the `AFMTOOL` folder in your Desktop, click into  `results` folder and then into `xlSheets` folder. The Excel file name is of the timestamped format `DDMMYYYYHHMM_AFMResults`, where the timestamp is the time when you started running the script (after you click `Open` in step 4). 
8. The script may not be able to detect the copper contact points perfectly, especialy for noisy data. It is recommended to do a quick check of the results produced by going to the `ML_identified_contacts` folder under `results` folder to check the copper metal contacts detected by the algorithm. If your Excel file is `DDMMYYYYHHMM_AFMResults`, then the corresponding folder to check under `ML_identified_contacts` has name `DDMMYYYYHHMM` with the same timestamp. As well as the center of the cirlces detected are not close to the edge of the actual contact, and the radius is not off by more than 20% the script should be able to obtain the corect regions for calculations. For a more accurate check, you can also check the folder `ref_regions_imgs` under `results` to see the exact regions used by the algorithm for calculations of the roughness, plotting line profile, and finding step height. 

### Additional Functions

One can add flags when running the script to customize the output. For instance, by default the program only evaluates roughness over the best 3 circles detected. One can make the script evaluate over all circles detected by adding the `-A` flag after step 3 under Usage section above. i.e.
```
python3 AFMTOOL.py -A
```
Below is a list of other flags that can be used. If multiple flags need to be used concurrently, just add the additional flags at the back. i.e. To use flag `-A` and `-mr` and `-Mr` concurrently, use the command

```
python3 AFMTOOL.py -A -mr 3 -Mr 6
```
Flags: 
  - -A: Evaluate roughness over all detected circles
  - -mr: Specify minimum radius of circles to be evaluated. Should be followed by a decimal/integer. `python3 AFMTOOL.py -mr 3` specifies a minimum radius of 3um. 
  -  -Mr: Specify maximum radius of circles to be evaluated. 
  - -p: Specify pitch (um). This will set the minimum distance between detected circles. 
  - -E: Exclude circles from calculation. If by looking at the reference images we find a small number of contacts are identified wrongly and we want to exclude them, we can use the `-E` flag followed by the list of indexes (Displayed at the bottom left of each green square) of circles to be excluded, separated by commas and not spaces. The listed circles will then be excluded from roughness calculations and will not be chosen for generation of line profile. E.g. If we want to exclude the first, third and fourth circles, use the following command:

  ```
  python3 AFMTOOL.py -E 1,3,4 

  ```

## Troubleshooting
- If after typing in `python3 AFMtool.py`, the File Explorer windows does not pop up after a long time (~20s), try pressing Ctrl+C to terminate the process. If the process terminates successfully, there should be a prompt message stating so. Then type in `python3 AFMtool.py` again to restart the process. If the terminal doesn't respond to Ctrl+C also, close the terminal and restart from step 1. 

## Assumptions made of AFM raw data formats
- x,y axis have range 20um (Hardcoded to eliminate user's need of entering range. If need to change, open root AFMTOOL folder in VSCode or other text editors and search '20' to see the places being hardcoded.)
- Diameter:Pitch ratio is at least 1:2 (Used in choosing area to calculate polymer roughness. If need to change, go to util/roughness/roughness.py and change the section on getting polymer roughness.)
- Contacts are circular. (Used in identifying copper contacts.)

## Notes for future maintenance/updates
### Functions of key folders/files
```
AFMTOOL/
├── /AFMTOOL/ 
│   ├── /util/              # Folder containing scripts grouped by their general functions (Draw 2D/3D plots, find roughness, find step height, etc)
│   ├── AFMtool.py          # Script that will be ran from command line, it'll call other scripts in the process of running when needed
├── /results/               # Test files (alternatively `spec` or `tests`)
    ├── /ref_regions_imgs/  # Place to store images indicating regions which are used for calculation of copper/polymer roughness and step height. 
    ├── /ML_identified_contacts  # Raw output from OpenCV Houghcircles indicating the circles identified, used to quickly check if script is giving correct result for each file. (Maybe can remove after completely verifying accuracy of ref_regions_imgs)                            
    └── /xlSheets           # Folder storing final Excel reports

```

## Development Timeline
- 6/5/2022: 
    - Able to generate 2D, 3D plots using .spm data using Python. (https://github.com/ChenJiakaiIME/AFMTool/tree/main/AFMTOOL/images) Color may need improvement.

- 9/5/2022: 
  - Machine learning script able to recognise circular metal contacts from 2D images generated. 
  - Enabled Excel reports to be automatically generated to show the data/images generated from raw data files.

- 10/5/2022: 
  - Enabled batch processing. User can select multiple files at once from window to be processed, added progress bar to show how many files have been processed in live time (https://github.com/ChenJiakaiIME/AFMTool/pull/4)
  - Auto generate Excel report with all images generated with their file names labelled (https://github.com/ChenJiakaiIME/AFMTool/pull/5)
  - Fine tuned ML scripts for contact points that are not nicely circular (https://github.com/ChenJiakaiIME/AFMTool/pull/2)
  - Enabled auto-saving of images of circles identified for manual checking of ML results

- 11/5/2022:
  - Enabled auto generation of line profile plot 
  - Auto calculation of roughness (Ra) at center of copper contacts

- 12/5/2022:
  - Able to calculate step height
  - Able to plot vertical lines on line profile denoting areas of copper contact and polymer
  - Insert line profile image and step height into Excel sheet
  - Able to calculate polymer roughness

- 13/5/2022:
  - Fixed decimal points to 2
  - Generated requirements.txt

- 19/5/2022:
  - Corrected for quadratic background 
  - Corrected coordinates for taking Ra
  - Added reference pictures row in Excel report to mark out on 2D diagram which areas are used for Ra calculations
  - Correct d.p to 3
  - Enlarged axis for 3D plot

- 20/5/2022:
  - Added ref image to mark regions for line profile and step height calculations
  - Corrected errors in step height calculations
  - Implemented multiple checks for circle recognition (If height data fail, use different color mapping, if fail again use phase data, if still fail use binary filter)
  - Updated docs for usage and installation instructions

- 23/5/2022:
  - Added calculations for roll off

- 30/5/2022:
  - Implemented flags that can be used to customize output. 

## Notes on possible changes to measurement methods
- Obtain step height using height histogram instead of line profile?
