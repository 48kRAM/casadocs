

# Image Masks 

Pixel by pixel selection via image masks

A mask can be used to define whether part of an image is used or not. There are different options for masks:

-   an image cube with Boolean True/False values: They usually live inside image cubes and are automatically applied to the data. More than one mask may exist in a cube. The task **makemask** (see [below](#image-mask-handling--makemask-)) can be used to access and manipulate internal Boolean masks via the image.im:mask syntax. 
-   an image cube with zero and non-zero values: They are their own image cubes and are applied to other image cubes when needed.
-   an LEL string for a condition.

 

# Masks (*mask parameter*)

Using image cubes is useful to mask on a pixel by pixel basis, where False and zeros mark masked (excluded) pixels (see also \'[LEL masks](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel/lel-masks)\'). Both versions can be converted into each other with the task **makemask**. Some analysis tasks show an optional *stretch* parameter which is useful, e.g., to expand a single plane mask to an entire cube along the spectral axis.

To use a different zero/non-zero mask (in this case *\'*myimage.mask*\'*), the parameter can be set like the following:

```
mask='mask(myimage.mask)'
```

The default boolean masks inside images will also be respected with the above syntax.

But remember that an image can have multiple Boolean masks, so to use the mask2 in an image, set the parameter as: 

```
mask='mask(myimage.mask:mask2)'
```

using the syntax where the mask is specified after the colon. To see what masks are present in your image, use the **makemask** task.

An [LEL string](#lattice-expressions--expr-) can be an on-the-fly (OTF) mask expression or refer to an image pixel mask.

Note that the mask file supplied in the *mask* parameter must have the same shape, same number of axes, and same axes length as the images supplied in the *expr* parameter, with one exception. The mask may be missing some of the axes --- if this is the case then the mask will be expanded along these axes to become the same shape.

The following example uses the mask from file ngc5921.clean.cleanbox.mask :

```
mask='mask(ngc5921.clean.cleanbox.mask)'
```

Here, the mask is calculated to be all pixels with values larger than 0.5:

```
mask='"ngc5921.clean.cleanbox.mask">0.5'
```

Because it is an LEL expression, care must be taken to properly escape characters which LEL views as special. For details, see the [LEL document](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel/lattice-expression-language). As an example, specifying

```
mask = "3clean_mask.im" (WILL FAIL)
```

will cause the image analysis application to fail, because the image name begins with a number. The solution is to escape the name properly, e.g.:

```
mask = "'3clean_mask.im'"
```

 

# Image Mask Handling (**makemask**) 

**makemask** facilitates the handling of image masks in CASA. As mentioned above, there are two basic mask formats: 1) one or more Boolean masks stored internally in the image file, and 2) images with zero and non-zero image values. **makemask** looks like:

```
#makemask :: Makes and manipulates image masks
mode                =     'list'        #Mask method (list, copy,expand,delete,setdefaultmask)
     inpimage       =         ''        #Name of input image.
```

To distinguish between Boolean internal masks and zero/non-zero images, **makemask** uses the syntax galaxy.image:mask0 for Boolean masks within an image: in this example, the Boolean mask mask0 within the image galaxy.image*.* Without the colon separator, the image itself will be treated as a zero/non-zero mask.*mode=\'list\'* lists all the internal Boolean masks that are present in an image. The default masks can be set with *mode=\'setdefaultmask\'* and they can be deleted with the *mode=\'delete\'*. The default mask is used when an image is displayed in the viewer and is used in all analysis tasks.*mode=\'copy\'* lets a user copy a Boolean mask from one image to another image, or to write out the Boolean mask as a zero/non-zero image. The latter format is very useful when different masks are combined or manipulated. All the image analysis tools, in particular **immath** are applicable for such zero/non-zero masks as they act like normal images. **makemask** will always attempt to regrid the input mask to the output image.In addition *mode=\'copy\'* can be used to merge masks and also accepts regions. E.g. to create a mask from a CASA region file, the input would look like:

```
#makemask :: Makes and manipulates image masks
mode                =     'copy'        #Mask method (list, copy,expand,delete,setdefaultmask)
     inpimage       = 'inputimage.im'   #Name of input image.
     inpmask        = 'region.crtf'    #mask(s) to be processed: image masks,T/F internal masks
                                        #(Need to include parent image names),regions(for copy mode)
     output         = 'imagemask.im'    #Name of output mask (imagename or imagename:internal_maskname)
     overwrite      =      False        #overwrite output if exists?
```

*mode=\'expand\'* furthermore expands a mask in the spectral domain. It regrids first then stretches the edge channels. E.g. a one plane continuum image would be stretched to all planes of a data cube.

 
