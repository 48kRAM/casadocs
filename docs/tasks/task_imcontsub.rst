

.. _Description:

Description
   imcontsub task: Estimates and subtracts continuum emission from an
   image cube
   
   For each direction pixel in an image (or a subset selected by
   *region* and/or *box*), this task estimates the continuum by
   fitting a polynomial to one or more subsets of the channels. In
   most cases, the user should choose the subset(s) of channels to be
   free of spectral lines. The continuum estimate is saved in
   *contfile* and subtracted from the image (or its subset) to make a
   spectral line estimate, which is saved in *linefile*.
   
   While imcontsub offers users the option to save the continuum
   estimate as a (multi-channel) dataset, the optimal way to create a
   continuum image is by using the multi-frequency synthesis (MFS)
   option in **tclean**.
   
   Note that fitting the continuum and subtracting it from a spectral
   line data set can also be done in the *(u,v)*-domain using the
   task **uvcontsub**.
   
    
   
   .. rubric:: Task-specific Parameter Descriptions
      
   
   .. rubric:: *linefile*
      
   
   Name of image to which to save the result of subtracting the
   computed continuum from the input image.
   
   .. rubric:: *contfile*
      
   
   The computed continuum image.
   
   .. rubric:: *fitorder*
      
   
   Order of polynomial to fit to the specified spectral channels to
   determine the continuum.
   
   .. rubric:: *chans*
      
   
   Spectral channels to use for fitting a polynomial to determine
   continuum.
   

.. _Examples:

Examples
   Fit a second order polynomial (fitorder=2) to channels 3-8 and
   54-60 to an RA x Dec x Frequency x Stokes cube, selecting the
   Stokes I plane
   
   ::
   
      | ch = '3~8, 54~60'
      | imcontsub(imagename="myimage.im", linefile="mycontsub.im",
        fitorder=2, chans=ch, fitorder=2, stokes="I")
   

.. _Development:

Development
   --CASA Developer--
   
   Here would be a discussion of how applycal is implemented.  This
   is intended for the other members of the development team so is a
   technical discussion.  We will work on building these up over
   time.
   