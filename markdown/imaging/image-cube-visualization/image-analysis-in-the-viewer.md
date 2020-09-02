

# Image Analysis in the Viewer 

Analysis Tools that are available in the Viewer

## The Brightness Profile Tool

The viewer allows the user to draw multiple line segments using the \"Polyline drawing\" button, and this feature can be used to display one-dimensional brightness profiles of images, such as shown in the [Spatial Profile Tool](#FigSlicerTool). After double-clicking the last line segment, the \'Regions\' dock will then display a preview of the slice in the Spatial Profile tab and the full \"Spatial Profile Tool\" can be launched from there by clicking the \"Spatial Profile Tool\" button. This \"Spatial Profile Tool\" panel allows one to select the interpolation method to connect the pixels, and a number count for the sampled pixels in between markers. \'Automatic\' will show all pixels. The x-axis of the display can be either the distance along the slice or the X and Y coordinate projections (e.g. along RA and DEC). All segments are also listed at the bottom with their start and end coordinates, the distance and the position angles of each slice segment. The color tool can be used to give each segment a separate color.

------------------------------------------------------------------------

 

![247c9434dc6e7bfcd4508140a7efbe0653671d1d](media/247c9434dc6e7bfcd4508140a7efbe0653671d1d.png)

------------------------------------------------------------------------

 

## The Histogram Tool

 

------------------------------------------------------------------------

![4bd76aea63562362de82fe6ddeeede1ce551317d](media/4bd76aea63562362de82fe6ddeeede1ce551317d.png)

------------------------------------------------------------------------

<div>

CASA can calculate and visualize a histogram of pixel values inside a region of interest. To examine this histogram, select Histogram from the Tools drop-down menu or the \'Histogram\' icon in the Main Toolbar (looks like a comb). This opens the full Histogram Tool; more limited versions are accessible from the Region Manager Panel, the graphical color table manipulation tool, and the Collapse/Moments tool.

The resulting Histogram Tool should look something like [Histogram Tool](#FigHistogramTool). The menus along the top (or the corresponding mouse clicks) allow one to:

-   Zoom to the full range, a selected percentile, or a graphical range.
-   Change the display of the histogram to show a log axis, display as either a line plot, an outline, or a filled histogram. Change the number of bins in the histogram, or clear the plot (to start over).
-   Configure what data are fed into the histogram. You can use this menu to tell the histogram to track the channel currently selected in the main Viewer Display Panel (click the \"Track Channel\" box) or to integrate across some range of channels (defaulting to the whole image). You can also switch the 2-D footprint used between the whole Image, the Selected Region, and All Regions.
-   Save (via the disk icon) an image of the histogram to a graphical file on disk.

The Histogram Tool also allows you to fit the distribution using either a Gaussian or a Poisson distribution, for example to estimate the noise in the image (a Gaussian will be a good choice to describe the noise in most radio data cubes). You can specify initial estimates or let the program generate initial guesses. The fit is then overplotted on the histogram (colors can be adjusted by clicking the color wheel icon in the toolbar) and details of the fit are printed to the text window below the fit button.

</div>

<div>

 

## The Two-Dimensional Fitting Tool

 

------------------------------------------------------------------------

![df2fff474cbd464f25d5e9bb87cd7107f61a5b87](media/df2fff474cbd464f25d5e9bb87cd7107f61a5b87.png)

------------------------------------------------------------------------

 

CASA can fit two-dimensional Gaussians to an intensity distribution, and the Two-Dimensional Fitting Tool in the Viewer exposes this functionality interactively. This tool, accessed by the \'blue circles\' icon in the Main Toolbar or the Tools:Fit menu item, has an interface like that shown in [Two-Dimensional Fitting Tool](#FigTwoDFitting). The interface exposes several options:

1.  You can select whether to fit only the selected region or the whole image plane and specify which channel of the cube you want to operate on.
    <div class="alert alert-info">
    **NOTE**: The two dimensional fitter only operates on a single channel at a time.
    </div>
2.  Initial Estimates: The box in the top left corner allows the user to specify initial estimates by feeding in a file. The easiest way to make an appropriate file is to edit an existing one. Even easier, you can use the Find Sources button to automatically generate a temporary file of initial estimates.
3.  Pixel Range: You can choose to only include a certain range of pixel intensity values in the fit. For example, you might choose to only fit Gaussians to pixels a few times above the measured noise level. You can use the Specify Graphically button to bring up an interactive histogram of the region (a reduced functionality version of the full Histogram Tool).
4.  Output: You can choose to save the output of the fit as a file to the specified directory and to subtract the fit from the image and to subtract the fit from the original, creating a Residual Image that gets stored as a CASA image and automatically loaded into the viewer. This gives a way to tell how well your fit describes the total emission.
5.  Visualization: You can toggle whether the fit is displayed on the viewer or not and change the color of the marker.

Click Fit to start the fit. If the fit does not converge, try improving your initial estimates and fitting again.

</div>
