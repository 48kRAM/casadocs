

# Wide Band Imaging 

MFS, MT-MFS with wide-field imaging,mosaics and wideband PB correction

# **Wideband imaging in CASA is [[experimental](https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/tasks-and-tools)] \sigma_{continuum} \propto \frac{T_{sys}}{\sqrt{ N_{ant}(N_{ant}-1) ~ N_{chan}\Delta\nu~ \Delta\tau}}= \frac{\sigma_{chan}}{\sqrt{N_{chan}} } \end{eqnarray}$$

where $T_{sys}$ is the instrumental system temperature, $\Delta\nu$ is the bandwidth of each channel, $\Delta\tau$ is the integration time, $N_{chan}$ is the number of frequency channels, and $\sigma_{continuum}$ and $\sigma_{chan}$ are theoretical wideband and narrowband image noise levels.  Note that this calculation is for an ideal system whose gain is flat across the band with equally weighted channels (i.e. at the center of the primary beam). 

To take full advantage of this broadband imaging sensitivity, image re-construction algorithms need to be sensitive to the effects of combining measurements from a large range of frequencies. These include frequency-dependent angular resolution and uv-coverage, frequency-dependent array element response functions, and the spectral structure of the sky brightness distribution.

![063c6f81181136f30f7270f39f42dd89443218e7](media/063c6f81181136f30f7270f39f42dd89443218e7.png){.image-inline width="466" height="223"}

 

## UV-Coverage

Projected baseline lengths are measured in units of the observed wavelength. Therefore the $uv$ coverage and the imaging properties of an interferometer change with frequency. As the observing frequency increases, the angular resolution for a given distribution of antennas increases (or, conversely the width of the point spread function given by $\theta_{\nu} = 1/{u}_{max}$ radians, decreases). In addition, at higher observing frequencies, the sensitivity to large spatial scales for a given distribution of antennas decreases. 

### Bandwidth Smearing (limits of channel averaging)

The choice of frequency resolution (or channel width) at which visibilities must be measured (or can be averaged up to) for synthesis imaging depends on the $uv$ grid cell size to be used during imaging, which in turn depends on the observed frequency and the desired field of view in the image. The following condition ensures that within a field of view chosen as the half power beam width of the antenna primary beam, the image-domain bandwidth smearing is smaller than the angular resolution of the instrument:$$\begin{eqnarray} \frac{\Delta \nu}{\nu_0} < \frac{Resolution}{FoV} = \frac{\lambda/b_{max}}{\lambda/D} = \frac{D}{b_{max}} ~~~~~ \Rightarrow ~~~~~ {\Delta \nu} < {\nu_0} \frac{D}{b_{max}}  \end{eqnarray}$$

For broad-band receivers, this limit will change across the band, and the channel width should be chosen as the bandwidth smearing limit computed for $\nu_{min}$.

 

## Sky Brightness

Stokes I continuum emission usually has smoothly varying, continuous spectral structure often following a power law functional form with curvature, steepening and turnovers at various locations in the spectrum. Power laws and polynomials are typically used to model such sky spectra. With the MT-MFS wideband imaging algorithm, a Taylor polynomial in $I$ vs $\nu$ space is fitted to the data per flux component, and the resulting coefficients used to calculate the spectral index that a power law model would provide. 

 

## Primary Beam

At the center of the primary beam, bandpass calibration makes the gain flat across the band. Away from the pointing-direction, however, the frequency-dependence of the primary-beam introduces artificial spectral structure in the wideband flux model reconstructed from the combined measurements. This frequency dependence must be modeled and removed before or during multi-frequency synthesis imaging to recover both spatial and spectral structure of the sky brightness across a large field of view.  In general, the frequency dependence of the primary beam can be approximated by a power law.

If $\theta$ is the angular distance from the pointing center and $\theta_0$ is the primary beam FWHM at the reference frequency, then the frequency dependence of the primary beam is equivalent to a spectral index of$$\begin{eqnarray} \alpha_{\rm E} &=&-8\log(2)\left(\frac{\theta}{\theta_0}\right)^2\left(\frac{\nu}{\nu_0}\right)^2 \end{eqnarray}$$

This corresponds to an effective spectral index of -1.4 at the half power point and reference frequency.

 

# Options in CASA for wideband imaging

<div class="alert alert-warning">
**WARNING**: Wideband mosaicing is still in its commissioning phase and not officially endorsed in CASA 5.5. With *deconvolver='mtmfs'* for multi-term imaging including wideband primary beam correction, *gridder='awproject'* has a known bug and should not be used. For *gridder='mosaic'* the uncertainties in the derived spectral index may be larger than the xxx.alpha.error images would imply, with or without the use of conjbeams, because of systematic issues that are currently being evaluated. Development/commissioning of wideband mosaicing is ongoing and will be available in a next CASA release.
</div>

 

## (1) MFS (nterms=1)

Traditionally, multi-frequency synthesis (MFS) imaging refers to gridding visibilities from multiple frequency channels onto a single spatial-frequency grid. It assumes that the sky brightness and the primary beam are constant across the total measured bandwidth and all frequencies measure the same visibility function just at different spatial frequencies. In this case, standard imaging and deconvolution algorithms can be used to construct an accurate continuum image.

For sources with spectral structure across the observed band, this approach converts any spectral variations of the visibility function into spurious spatial structure that does not follow the standard convolution equation in the image domain and therefore will not self-correct during deconvolution.  For the VLA at L-Band, for example, a 1.0 Jy source with spectral index of -1.0 across the 1-2 GHz band will produce spectral artifacts at the $5\times10^{-3}$ level. Therefore, sources requiring dynamic ranges (peak brightness / thermal noise) less than a few hundred will not see any of these artifacts and basic MFS imaging will suffice. Detection experiments in otherwise empty fields are a good example of when this method is most appropriate.

 

## (2) MT-MFS (nterms\>1)

To alleviate the spectral artifacts discussed above and to reconstruct the broad-band sky brightness distribution correctly, a spectral model must be folded into the reconstruction process. The advantages of such an image reconstruction are that the combined $uv$ coverage (from all channels) is used, flux components are \'tied\' across frequency by the use of an explicit spectral model or physically motivated constraints, and the angular resolution of the resulting intensity and spectral index images is not limited to that of the lowest frequency in the band. Under high signal-to-noise conditions, the angular resolution follows that of the highest frequency in the band.  Disadvantages are that the reconstruction is often tied to a specific spectral model and will work optimally only for sources whose spectral structure can be described by that model (i.e.a low order Taylor polynomial). In low signal-to-noise situations, the unnecessary fitting of higher order terms can increase the noise and error in the results.

The MTMFS algorithm models the spectrum of each flux component by a Taylor series expansion about $\nu_0$ .$$\begin{eqnarray} \vec{I}^{m}_{\nu} = \sum_{t=0}^{N_t -1} {w_{\nu}^{t}} \vec{I}^{sky}_{t} ~~~\mathrm{where}~~~ w_{\nu}^{t}&=&{ \left( \frac{\nu - \nu_0}{\nu_0} \right) }^t  \end{eqnarray}$$where $I^{sky}_t$ represents a multi-scale Taylor coefficient image,and $N_t$ is the order of the Taylor series expansion.

A Taylor expansion of a power law yields the following expressions for the first three coefficients from which the spectral index $I^{sky}_{\alpha}$ and curvature $I^{sky}_{\beta}$ images can be computed algebraically.$$\begin{equation} I^m_0 = I^{sky}_{\nu_0} ~~;~~ I^m_1 = I^{sky}_{\alpha} I^{sky}_{\nu_0} ~~;~~ I^m_2 = \left(\frac{I^{sky}_{\alpha}(I^{sky}_{\alpha}-1)}{2} + I^{sky}_{\beta}\right) I^{sky}_{\nu_0} \end{equation}$$Note that with this choice of parameterization, we are using a polynomial to model a power-law.

 

 

### User controls

#### Reference Frequency

This is the frequency about which the Taylor expansion is done. The default is the center of the frequency range being imaged, but this is not required.  The relative weights/flags of data on either side of this frequency should be inspected to ensure that the reconstruction is not ill-conditioned. The output intensity image represents the flux at this reference frequency. Please note that the value at a specific reference frequency is different from the integrated flux across a frequency range.

#### nterms

The number of Taylor coefficients to solve for is a user parameter.  The optimal number of Taylor terms depends on the available signal-to-noise ratio, bandwidth ratio and spectral shape of the source as seen by the telescope (sky spectrum x PB spectrum). In general, *nterms*=2 is a good starting point for wideband EVLA imaging and the lower frequency bands of ALMA (when fractional bandwidth is greater than 10%) if there is at least one bright source for which a dynamic range of greater than few 100 is desired. Spectral artifacts for the VLA often look like spokes radiating out from a bright source (i.e. in the image made with standard mfs imaging).  If increasing the number of terms does not eliminate these artifacts, check the data for inadequate bandpass calibration. If the source is away from the pointing center, consider including wide-field corrections too.

The signal-to-noise ratio of the source must also be considered when choosing nterms. Note that the Taylor polynomial is in I vs $\nu$ space. This means that even for a pure power law, one may need nterms=3 or 4 in order to properly fit the data if there is adequate signal to see more spectral variation than a straight line. One should avoid trying to fit a high-order polynomial to low signal-to-noise data. 

 

 

### Data Products

#### Taylor Coefficient Images

The basic products of the MT-MFS algorithm are a set of $N+1$ (multi-scale) Taylor coefficient images that describe the spectrum of the sky brightness at each pixel (coefficients of an $N^{th}$-order polynomial). The $0^{th}$-order coefficient image is the Stokes I intensity image at the reference frequency.

#### Multi-Term Restoration

The restoration step of the MT-MFS algorithm performs two actions in addition to the standard convolution of the model with a Gaussian beam and adding back of the residuals. First, it converts the residuals into the Taylor coefficient space before adding them to the smoothed model components (which are already Taylor coefficients). The residuals (or error) will typically be higher for higher order terms. Since the terms are not strictly independent, errors from including higher order terms may slightly increase the noise floor even on the zeroth order intensity image.  This arises because the concept of a \'residual image\' is different for a multi-term algorithm. For standard narrow-band imaging, the residual or dirty image already has sky-domain fluxes.  For multi-term imaging, the residual or dirty image must be further processed to calculate Taylor coefficients which represent sky-domain fluxes. It is this step that will provide accurate spectral indices (for example) from undeconvolved dirty images (i.e. tclean runs with niter=0 and deconvolver=\'mtmfs\').

#### Calculating Spectral Index

Spectral index is computed as $I^{sky}_{\alpha} =  I^m_1 /  I^m_0$, for all pixels above a threshold applied to the $I^m_0$. Other pixels are zeroed out and a mask is applied.  Currently this threshold is automatically calculated to be 5 x max( peak residual, user threshold ).  Right now, the spectral index calculation can be modified  in two ways (a) perform the above division oneself in a python script or (b) use the widebandpbcor task with action=\'calcalpha\'.   The ability to control this within tclean itself will be added in the future.

Spectral curvature (when possible) is also computed from the Taylor coefficients.

#### Calculating Error in Spectral Index

An estimate of spectral index error is also provided as an output image. This is an empirical error estimate derived as the result of error propagation through the division of two noisy numbers: alpha = tt1/tt0 where the \'error\' on tt1 and tt0 are just the values from the residual coefficient images at each pixel. In the limit of perfect deconvolution and noise-like residuals, this number can be accurate. However, in practice, deconvolution artifacts usually remain in the residual image (especially underneath extended emission) and they dominate the errors. In general, the spectral index error map should only be used as a guide of which regions of the image to trust relative to others, and not to use the absolute value of error for scientific analysis.  A more useful error estimate can be derived by repeating the imaging run (especially if it involves multi-scale components) with slightly different settings of scale sizes and iteration controls, to see what is true signal and what can be attributed to reconstruction uncertainty.  For high signal-to-noise compact sources, error limits of $\pm 0.05$ can be achieved. For complicated extended emission at about SNR=100 or less, typical errors are about $\pm 0.2$.  These errors are highly correlated with how appropriately the scale sizes are chosen, with errors ranging from $\pm 0.1$ or less up to $\pm 0.5$ in the limit of using delta functions to try to model extended emission.

Errors on spectral curvature are much higher than for spectral index. In one example where the M87 galaxy was imaged at L-Band, only the central bright inner lobes (at dynamic range of a few thousand) showed average spectral curvature that could be trusted.

## (3) Cube + imcollapse.

The simplest form of wideband imaging is to treat each frequency channel independently and make an image cube. A continuum image can then be formed by first smoothing all planes to a common (lowest) angular resolution and computing the mean across frequency. Spectral structure can be modeled per pixel from this smoothed cube. The main advantage of this method is its simplicity and the fact that it does not depend on any particular spectral model. The main disadvantage is that the angular resolution of all higher frequency channels must be degraded to that of the lowest frequency before any combined analysis can be done. Also, in case of complicated spatial structure, each frequency\'s $uv$ coverage may be insufficient to guarantee reconstructions that are consistent with each other across the band.

# Comparison of different wideband imaging methods

 

  --------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                         Cube                                                                                                                                                                        MFS                                                                                                                                                                              MFS with a wideband model

  Angular Resolution                                                               Same angular resolution as lowest frequency data                                                                                                                           Same angular resolution as highest frequency data                                                                                                                                           Same angular resolution as highest frequency data

  Continuum Sensitivity                                                                    Narrow-band (for deconvolution)\                                                                                                                                                          Full                                                                                                                                                                                        Full
                                                                                                           \                                                                                                                                                                                                                                                                                     
                                                                                                 Full (after stacking)                                                                                                                                                                                                                                                                           

  Weak Sources                                              Low SNR sources may not be deconvolved accurately in all channels, diluting the combined result                                                               Accurate low SNR imaging, but ignores spectral variation of bright sources. Errors show up at dynamic ranges of a few 100.                                                                                             Accurate bright source modeling to allow detection of weak sources.

  Strong Sources                                                         Can handle arbitrary spectra down to the single channel sensitivity.                                                                                                                                  Ignores Spectra                                                                                                                                                             Models spectra. Most useful for strong sources.

  Extended Emission                        Fewer constraints per channel so reconstruction may not match across channels. This leads to errors when computing spectral index                                                                 Uses full spatial frequency coverage but ignores spectral. This can cause artifacts.                                                                                                   Reconstructs structure and spectra accurately but depends on the spectral model for accuracy.

  Spectral Reconstruction                                      Accurate for simple bright sources and does not depend on any predefined spectral model.                                                                                                                        Ignores spectra                                                                                                                                                    Models spectra using a wideband flux model during reconstruction.

  Primary Beam correction (and mosaics)                                    Per channel, can be done either during gridding or after imaging                                    Since an MFS image is a weighted channel average, accurate PB correction must be done per channel before combination. Post deconvolution division by a wideband primary beam is also a reasonable approximation.   Wideband PB correction must be done either during gridding or after imaging by dividing out the primary beam and its frequency dependence from the obtained model.
  --------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------

 

 

 

#  Other uses of wideband models

## Wideband Self Calibration

The broad-band flux model generated by the MS-MFS algorithm can be used within a self-calibration loop in exactly the same manner as standard self-calibration. The purpose of such a self-calibration would be to improve the accuracy of the bandpass calibration and maintain smoothness across spectral windows or subbands that may have been treated independently.

## Continuum Subtraction

In the case of accurate deconvolution, the wideband model may be subtracted out to study line emission on top of the continuum. The wideband model would be made by excluding channels that contain known line emission,  predicting the wideband model over the entire frequency range, and then performing a \'uvsub\' to subtract it out.

# Example

The following images of 3C286 illustrate what wideband imaging artifacts look like and how they change with different values of nterms.  These images were made from about 15 minutes of VLA L-Band calibrator data (1-2 GHz).  Note that such clear improvements in the imaging will be visible only if there aren\'t any other sources of error (e.g. calibration errors or weak residual RFI).

 

![d3af02dfa60a934b1cff3aafac93d0b2919b89d5](media/d3af02dfa60a934b1cff3aafac93d0b2919b89d5.png){.image-inline width="549" height="341"}

 


# Wide-Band and Wide-Field Imaging 

## Wide-Band + W-term

W-Projection or faceted imaging can be combined with multi-term imaging (*specmode*=\'mfs\', *deconvolver*=\'mtmfs\', *gridder*=\'widefield\' or \'wproject\'). The two algorithms are distinct enough there there are no special considerations to keep in mind when combining them. 

## Wide-Band + Full Beam

The frequency dependence of the primary beam introduces artificial spectral structure on the sky brightness distribution away from the pointing center.  Below is an example of what this spectral structure looks like, in terms of a power law spectral index.  If nothing is done to eliminate the artificial PB spectrum, it will be visible to the minor cycle during deconvolution and will be interpreted as extra sky spectral structure.   Another aspect of using a wide-band primary beam is the large shelf of continuum sensitivity outside the main lobe of the average beam. This is also a region where the PB spectrum will be varying by up to 100% in positive and negative directions, also in a time-variable way. Therefore, there is increased sensitivity to sources outside the main lobe of the average PB, but very little hope of accurately imaging them without methods that carefully incorporate time- and frequency-dependent primary beam models. 

![dcb7b7bb1677f24cffedcd93d0d1b98c2e68fa9e](media/dcb7b7bb1677f24cffedcd93d0d1b98c2e68fa9e.png){.image-inline width="505" height="361"}

 

Three methods to handle wide band primary beams are discussed below. 

### Cube Imaging

The option of cube imaging is always present, where the primary beam is corrected per channel at the end of imaging, using appropriate frequency-dependent primary beam models.

### Post-deconvolution Wide-band Primary Beam Correction

If primary beams are ignored during imaging (gridders other than \'awproject\' or \'mosaic\'), the artificial spectral structure will be absorbed into the sky model (to the extent that it is possible, given that the primary beams are squinted and rotating, creating a time-varying primary beam spectrum).  The output Taylor coefficient images now represent the spectral structure of (primary beam) x sky.   

Wide-band primary beam correction can be done by constructing Taylor coefficients that represent the primary beam spectrum at each pixel, and applying a polynomial division to take them out of the output images (per pixel).

Steps: (1) Compute a set of primary beams at the specified frequencies(2) Calculate Taylor-coefficient images that represent the primary beam spectrum(3) Perform a polynomial division to primary beam correct the output Taylor-coefficient images from the MT-MFS algorithm(4) Recompute spectral index (and curvature) using the corrected Taylor-coefficient images.

Currently, the widebandpbcor task performs this function, but it is scheduled to move into tclean where it will be implemented within C++, and use internally generated information about relative spectral weights.

### Wideband AW-Projection

The use of *wbawp*=True with *gridder*=\'awproject\' and *conjbeams*=True enables conjugate beams to be used during gridding. The goal is to remove the frequency dependence of the primary beam during the gridding step so that the minor cycle sees the spectral structure of only the sky. This reduces the number of Taylor terms required to model the spectrum and removes the need for any primary beam correction on the output spectral index maps. 

Setting *wbawp=True* enables use of PB evaluated at the center frequency of each spectral window.  Setting *conjbeams=True* enables use of the PB at the \"conjugate\" frequency which effectively projects-out the scaling of the PB with frequency (see Bhatnagar et al, ApJ, [2013,Vol.770, No. 2, 91)](http://stacks.iop.org/0004-637X/770/91) .  The following plot shows the frequency dependence of a PB as a function of distance from the center of the PB.  The red curves trance the total-power response of the antenna and the blue curves show the frequency dependence of the antenna response.  The second figure below shows the effective frequency dependence when using conjugate beams duing imaging.  The blue curve is significantly flat compared to the plot in the first figure. When imaged with conjugate beams, the effects of frequency dependent PBs is effectively removed in the images fed to the minor cycle algorithms.  Image-plane based wide-band algorithms (like the MT-MFS algorithm) designed to model *only* sky frequency dependence can therefore be used without modification.

![794630806bc8bfbf48a70d1f523bda4845f764e4](media/794630806bc8bfbf48a70d1f523bda4845f764e4.png){.image-inline width="292" height="220"}![1dfad9084557b0bb6d968f7b37d6d964809f3515](media/1dfad9084557b0bb6d968f7b37d6d964809f3515.png){.image-inline width="292" height="220"}

## Wideband + Mosaics

There are several ways of constructing wideband mosaics. The three main choices are spectral (cube vs. MT-MFS), spatial (linear vs. joint mosaics), and primary beam correction (post-deconvolution corrections vs A-Projection based approaches that account for primary beams during gridding with or without correction of the frequency dependence at that stage).  This results to a large number of options for the user.  It is important to note that all methods have trade-offs and are not likely to give identical results (especially since in our software, different algorithms currently use different PB models).

It is recommended that when possible, to use  *specmode*=\'mfs\', *deconvolver*=\'mtmfs\' with *gridder*=\'awproject\' and *wbawp*=True in order to make wideband mosaics.  For cube-based wideband mosaic imaging, it is recommended that one uses *gridder*=\'awproject\' or \'mosaic\' per channel with a post-deconvolution primary beam-correction per channel.

 

### Wideband Mosaic Primary Beam

In a joint mosaic, one must keep in mind the spectral structure of the primary beam. In a single pointing, the spurious spectral structure is significant only away from the pointing center. Therefore, wideband options may not be required if the source of interest covers a small region at the center of the beam and if its own spectral structure isn\'t strong enough to warrant multi-term imaging.   However, in a mosaic, this primary beam spectral structure is present across the entire field of view of the mosaic, making even the imaging of flat-spectrum compact sources an exercise in wide-field and wide-band imaging.

 

![2012a00c1e7ad86ceadf38e2f3003013a18d8483](media/2012a00c1e7ad86ceadf38e2f3003013a18d8483.png){.image-inline width="454" height="175"}

 

 

 

 

 

# Bibliography

1. Rau\ &\ Cornwell\ (2011), A&A\ 532,\ A71\ (
^
