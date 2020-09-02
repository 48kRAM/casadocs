

# Water Vapor Radiometers 

Create phase correction gain table from ALMA Water Vapor Radiometer (WVR) data

The task **wvrgcal** generates a gain table based on Water Vapor Radiometer (WVR) data and is used for ALMA data reduction. Briefly, the task enables a Bayesian approach to calculating the coefficients that convert the outputs of the ALMA 183 GHz water-vapor radiometers (mounted on each antenna) into estimates of path fluctuations which can then be used to correct the observed interferometric visibilities.

The CASA task is an interface to the executable wvrgcal, which is part of the CASA 5 distribution and can also be called from outside CASA. The wvrgcal software is based on the libair and libbnmin libraries which were developed by Bojan Nikolic at the University of Cambridge as part of EU FP6 ALMA Enhancement program. CASA 5 contains version 2.1 of wvrgcal. The algorithmic core of wvrgcal is described in three ALMA memos (number 587 [\[1\]](#Bibliography), 588  [\[2\]](#Bibliography), and 593 [\[3\]](#Bibliography) ) which describe the algorithms implemented in the software.

The CASA task interface to wvrgcal follows closely the interface of the shell executable at the same time staying within the CASA task parameter conventions. In ALMA data, the WVR measurements belonging to a given observation are contained in the ASDM for that observation. After conversion to an MS using **importasdm**, the WVR information can be found in separate spectral windows. As of April 2016, it is still one single spectral window for all WVRs, however, the ID of the spectral window may vary between datasets. The **wvrgcal** task identifies the SPW autonomously, but it can also be specified via the parameter *wvrspw* (see below). The specified spectral window(s) must be present in the MS for **wvrgcal** to work. This is not to be mixed up with the list of spectral windows for which solutions should be calculated and which can be specified with the parameter *spw*. Note that **wvrgcal** will calculate a correction only for the scans with the words ON_SOURCE, SIGNAL, or REFERENCE in the scan intent. The various features of **wvrgcal** are then controlled by a number of task parameters (see the list above). They have default values which will work for ALMA data. An example for a typical **wvrgcal** call can be found in the ALMA CASA guide for the NGC 3256 analysis:

```
wvrgcal(vis='uid___A002_X1d54a1_X5.ms',
     caltable='cal-wvr-uid___A002_X1d54a1_X5.W',
     toffset=-1,
     segsource=True, tie=["Titan,1037-295,NGC3256"], statsource="1037-295",
     wvrspw=[4],
     spw=[17,19,21,23])
```

Here, *vis* is the name of input visibility file which as mentioned above also contains the WVR data and *caltable* is the name of the output gain calibration table. WVR data is typically in spectral window 0, but in the example above, the data are contained in spectral window 4. Although **wvrgcal** should automatically identify this SPW, it is explicitly specified with the *wvrspw* parameter in the above example. The *toffset* parameter is the known time offset in seconds between the WVR measurements and the visibility integrations for which they are valid. For ALMA, this offset is presently -1 s (which is also the default value).

The parameter *segsource* (segregate source) controls whether separate coefficients are calculated for each source. The default value True is the recommended one for ALMA. When *segsource* is True, the subparameter *tie* is available. It permits the formation of groups of sources for which common coefficients are calculated as well as possible. The *tie* parameter ensures best possible phase transfer between a group of sources. In general it is recommended to tie together all of the sources in a single Science Goal (in ALMA speak) and their phase calibrator(s). The recommended maximum angular distance up to which two sources can be tied is 15 degrees. The parameter statsource controls for which sources statistics are calculated and displayed in the logger. This has no influence on the generated calibration table.

Via the parameter *spw*, one can control for which of the input spectral windows **wvrgcal** will calculate phase corrections and store them in the output calibration table. By default, solutions for all spectral windows are written except for the ones containing WVR data. The **wvrgcal** task respects the flags in the Main and ANTENNA table of the MS. The parameter *mingoodfrac* lets the user set a requirement on the minimum fraction of good measurements for accepting the WVR data from an antenna. If antennas are flagged, their WVR solution is interpolated from the three nearest neighboring antennas. This process can be controlled with the new parameters *maxdistm* and *minnumants*. The former sets the maximum distance an antenna used for interpolation may have from the flagged one. And *minnumants* sets how many near antennas there have to be for interpolation to take place. For more details on the WVR Phase correction, see also the the ALMA Memo "Quality Control of WVR Phase Correction Based on Differences Between WVR Channels" by B. Nikolic, R. C. Bolton & J. S. Richer [\[4\]](#Bibliography) , see also ALMA memo 593 [\[3\]](#Bibliography).

###  Statistical parameters shown in the logger output of wvrgcal

The **wvrgcal** task writes out a variety of information to the logger, including various statistical measures of the performance. This allows the user to judge whether WVR correction is appropriate for the MS, to check whether any antennas have problematic WVR values, and to examine the predicted performance of the WVR correction when applied. For each set of correction coefficients which are calculated (the number of coefficient sets are controlled by the parameters *nsol*, *segsource* and *tie*), the **wvrgcal** output to the logger first of all shows the time sample, the individual temperatures of each of the four WVR channels, and the elevation of the source in question at that time. For each of these coefficient sets, it then gives the evidence of the bayesian parameter estimation, the calculated precipitable water vapor (PWV) and its error in mm, and the correction coefficients found for each WVR channel (dTdL).

The output then shows the statistical information about the observation. First of all it gives the start and end times for the parts of the observation used to calculate these statistics (controlled by *segsource*). It then shows a break down for each of the antennas in the data set. This gives the antenna name and number; whether or not it has a WVR (column WVR); whether or not it has been flagged (column FLAG); the RMS of the path length variation with time towards that antenna (column RMS); and the discrepancy between the RMS path length calculated separately for different WVR channels (column Disc.). These values allow the user to see if an individual WVR appears to have been suffering from problems during the observation, and to flag that antenna using *wvrflag* if necessary. This discrepancy value, Disc., can in addition be used as a simple diagnostic tool to evaluate whether or not the WVR correction caltable created by **wvrgcal** should be applied. In the event of the WVR observations being contaminated by strong cloud emission in the atmosphere, the attempt by **wvrgcal** to fit the water vapor line may not be successful, and applying the produced calibration table can in extreme cases reduce the quality of the data. However, these weather conditions should identified by a high value in the discrepancy column produced when running **wvrgcal**.

Discrepancy values of greater than a 1000 microns usually indicate strong cloud contamination of the WVR data, and the output calibration table should probably not be applied. If the values are between 100 and 1000 microns, then the user should manually examine the phases before and after applying the caltable to decide if WVR correction is appropriate. Work is underway at ALMA to provide additional routines to at least partially remove the cloud component from the WVR data before calculating phase corrections. CASA 4.7 will contain a first tested version of such a tool. After the antenna-by-antenna statistics, the output then displays some estimates of the performance of the **wvrgcal** correction. These are the thermal contribution from the water vapor to the path fluctuations per antenna (in microns), the largest path fluctuation found on a baseline (in microns), and the expected error on the path length calculated for each baseline due to the error in the coefficients (in microns).

###  Antenna position calculation

The information about antenna pointing direction is by default taken from the POINTING table. Should this table not be present for some reason, the user can instead switch to determining the antenna positions from the phase directions in the FIELD table (under the assumption that all antennas were pointing ideally). The switch is performed by setting the parameter *usefieldtab* to True.

###  Spectral window selection

By default, **wvrgcal** puts solutions for all spectral windows of the MS into the output calibration table. Since usually only the spectral windows are of interest in which the science target and the calibrators were observed, it is not necessary to store solutions for other spectral windows. The spectral windows for which solutions are stored can be selected with the parameter *spw*, e.g. spw = \[17,19,21,23\] will make **wvrgcal** write only solutions for spectral windows 17, 19, 21, and 23. With respect to the input WVR spectral windows, **wvrgcal** will by default regard all windows with 4 channels as WVR data. In typical ALMA data there is only one such spectral window in each ASDM. This may change in the future. In any case, the input WVR spectral window(s) can be selected with the optional parameter *wvrspw*. The syntax is the same as for the parameter *spw* above.

 

 

 

 

# Bibliography

1. [ALMA\ Memo\ 587](http://library.nrao.edu/public/memos/alma/memo587.pdf)\ 
2. [ALMA\ Memo\ 588](http://library.nrao.edu/public/memos/alma/memo588.pdf)\ 
3. [ALMA\ Memo\ 593](http://library.nrao.edu/public/memos/alma/memo593.pdf)\ 
4. [ALMA\ Memo\ "Quality\ Control\ of\ WVR\ Phase\ Correction\ Based\ on\ Differences\ Between\ WVR\ Channels"](https://casa.nrao.edu/Memos/memoqachannels.pdf)\ 
^
