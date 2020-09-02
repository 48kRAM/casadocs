

# On-the-fly calibration 

Performing on-the-fly calibration using mstransform

As of CASA 4.5 **mstransform** incorporates the possibility of applying on the-the-fly (OTF) calibration by specifying *docallib* = True, which in turn allows to specify the "Cal Library" filename (*callib* parameter). This transformation is the first one applied to the data, producing effectively a corrected data column on-the-fly, which can be further transformed. *callib* is the filename pointing to the calibration specification file. Details on how to specify the Cal Library file can be found on [this CASA Docs page](https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/cal-library-syntax), where conventions and current limitations are also described. The combination of OTF calibration and cal libraries enable complex calibrations to be applied, and for the calculation to proceed more quickly than they otherwise might.

```
docallib = True   #Enable OTF calibration

callib   = ''     #Cal Library filename
```

An example of a Cal Library file is given below.

    caltable='ngc5921_regression/ngc5921.bcal' calwt=True tinterp='nearest' 
    caltable='ngc5921_regression/ngc5921.fluxscale' calwt=True tinterp='nearest' fldmap='nearest' 
    caltable='ngc5921_regression/ngc5921.gcal' calwt=True field='0' tinterp='nearest' fldmap=[0] 
    caltable='ngc5921_regression/ngc5921.gcal' calwt=True field='1,2' tinterp='linear' fldmap='1' 

<div class="alert alert-info">
See the full description of a Cal Library [here](https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/cal-library-syntax).
</div>
