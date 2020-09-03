#
# stub function definition file for docstring parsing
#

def concat(vis, concatvis='', freqtol='', dirtol='', respectname=False, timesort=False, copypointing=True, visweightscale=[''], forcesingleephemfield=''):
    r"""
Concatenate several visibility data sets.

Parameters
   - **vis** (stringArray) - Name of input visibility file
   - **concatvis** (string='') - Name of output visibility file
   - **freqtol** (variant='') - Frequency shift tolerance for considering data as the same spwid
   - **dirtol** (variant='') - Direction shift tolerance for considering data as the same field
   - **respectname** (bool=False) - If true, fields with a different name are not merged even if their direction agrees
   - **timesort** (bool=False) - If true, sort by TIME in ascending order
   - **copypointing** (bool=True) - Copy all rows of the POINTING table.
   - **visweightscale** (doubleArray=['']) - List of the weight scaling factors to be applied to the individual MSs
   - **forcesingleephemfield** (variant='') - Make sure that there is only one joint ephemeris for every field in this list


Description
   This task concatenates several visibility data sets into a single
   MeasurementSet (MS).

   

   .. rubric:: Input and outputMeasurementSets
      

   The list of data sets given in the *vis* argument are
   chronologically concatenated into an output data set (named in
   *concatvis*), i.e. the data sets in *vis* are first ordered by the
   time of their earliest integration and then concatenated.

   For example, *vis =
   ['src2.ms','ngc5921.ms','ngc315.ms'],concatvis = 'src2.ms'.*

   If *concatvis* already exists (e.g., it is the same as the first
   input data set), then the other input data sets will be appended
   to the *concatvis* data set. There is no limit to the number of
   input data sets. If none of the input data sets has any scratch
   columns (model or corrected columns), none is created in the
   *concatvis*. Otherwise these columns are created on output and
   initialized to their default value (1 in model column, data in
   corrected column) for those data with no input scratch columns.

   .. note:: **NOTE**: If the*concatvis* outputfile exits on disk then the
      input files are added to this file. Otherwise the new file
      contains the concatenated data. Be careful here when
      concatenating to an existing file.

   

   .. rubric:: Spectral and position shift tolerances
      

   Spectral windows for each data set with the same channelization
   (equal numbers of channels), and within a specified frequency
   tolerance (parameter *freqtol*) of another data set, will be
   combined into one spectral window. By default,*freqtol* = '',
   which is understood by CASA to be a frequency tolerance of 1 Hz.
   For example,*freqtol = '10MHz'* will not combine spectral
   windowsunless they are within 10 MHz of each other.

   .. note:: **NOTE**: This option is useful to combine spectral windows
      with very slight frequency differences caused by Doppler
      tracking, for example.

   A field position in one data set that is within a specified
   direction tolerance (parameter *dirtol*) of another field position
   in any other data set will be combined into one field. The field
   names need not be the same -- only their position is used. In
   these cases, the actual direction and field name in the resulting,
   merged output field will be the ones from the
   chronologically-first input MS. Each appended dataset is assigned
   a new observation ID (provided the entries in the observation
   table are indeed different). By default,*dirtol* = '', which is
   understood by CASA to be a position tolerance of 1 milliarcsec
   (mas). Forexample,*dirtol = '1arcsec'* will not combine fields
   unless their phase centers differ by less than 1 arcsec. If the
   field names are different in the input data sets, the name in the
   output data set will be the first relevant data set in the list.
   Use the parameter*respectname = True* to indicate thatfields
   witha different name should not be merged even if their direction
   agrees (within*dirtol*).

   .. note:: **NOTE**: There is no constraint on data that is simultaneously
      observed for more than one field; for example multi-source
      correlation of VLBA data.

   

   .. rubric:: Operations performed on outputMeasurementSets
      

   Use the parameter*timesort = True* to sort the output visibility
   table in time.

   Set*copypointing = True*(the default behavior) to make a proper
   copy of the POINTING subtable (though this can be time-consuming).
   If *False*, the result is an empty POINTING table.

   The weights of the individual MSs will be scaled in the
   concatenated output MS by the factors in the list given in
   *visweightscale*. SIGMA will be scaled by 1/sqrt(factor). This
   parameter is useful for handling heterogeneous arrays. Use plotms
   to inspect the "Wt" columns as reference for determining the
   scaling factors. For example,*visweightscale* =[1.,3.,3.] will
   scale the weights of the second and third MS by a factor 3 and the
   SIGMA column of these MSs by a factor 1/sqrt(3).

   By default, **concat** will only merge two ephemeris fields if the
   first ephemeris covers the time range of the second. Otherwise,
   two separate fields with separate ephemerides are placed in the
   output MS. In order to override this behaviour and
   force**concat** to merge the non-overlapping or only partially
   overlapping input ephemerides, the name or IDof the field in
   question needs to be placed into the list in parameter
   *forcesingleephemfield*. For example, *forcesingleephemfield
   =*['Neptune'] will make sure that there is only one joint
   ephemeris for field Neptune in the output MS.

    """
    pass