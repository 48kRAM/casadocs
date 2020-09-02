

# Documentation Validation 

Process for validation of user documentation (content review)

# **Before You Start **

1.  Make sure you log into plone so that any pages currently marked \"private\" are visible to you.
2.  Please locate and review the current (4.7.0) inline help and any current online help page ([CASA Task Reference Manual](https://casa.nrao.edu/docs/TaskRef/TaskRef.html), [CASA Toolkit Reference Manual](https://casa.nrao.edu/docs/CasaRef/CasaRef.html)) for tasks and tools, and the relevant section of the [CASA Cookbook ](https://casa.nrao.edu/casa_cookbook.pdf) for chapters, for context for the assigned documentation review.
3.  Take a quick tour of plone by clicking the wrench in the upper right corner \--\> \"Tutorials\" \--\> \"Introduction\". It will show you several messages pointing out the different features of plone.

# **Testing Plan**

## Editorial Content and Style

Note: Validators should plan to make minor document changes directly to the document. Extensive changes should be reported back to the author using the appropriate JIRA ticket.

### Basic things

1.  Identify and correct typos, spelling, and grammatical mistakes.
2.  Confirm that all hyperlinks work properly.
3.  Does the content conform to common writing best practices (use of consistent tense, personal pronouns, etc.)?

### Internal consistency

1.  Throughout the text, please make sure that the following terms are used correctly (i.e., \"MeasurementSet\" is correct, not \"Measurement Set\"):
    -   MeasurementSet,
    -   Multi-MS,
    -   Sub-MS,
    -   MS,
    -   MMS
2.  If you are reviewing a Chapter, please make sure that links to subpages on the \"front\" page (where all of the subpages are listed) each contain a one-line description of that subpage\'s content. Links to the tasks and tools do not need this. For example, see the [Single Dish Calibration chapter front page](https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/single-dish-calibration). If the descriptions are missing, please add one.  

### Document hierarchy

1.  Is the location of this document in the plone hierarchy sensible?
2.  Does the page fit in well with chapters that come before and after it?

## Scientific/Relevant User Content

### Completeness

1.  For validating pages in the Global Task List or Global Tool List, when you type \"inp taskname\" in CASA, is every parameter that is listed documented to the same extent in plone? Please refer back to CASA 4.7 to see the pre-plone-migration versions of the inline help files. Between the \"Description\" and \"Parameters\" tabs, are there adequate explanations for every parameter in the task?
2.  Has old, non-relevant text that refers to earlier CASA versions been removed?
3.  We need to compile references to specific tasks and tools in each Documentation Chapter, which should appear as links within the Chapter. These should already be set up, but if there are additional links that are necessary, please create them within the Chapter folder following the existing examples. 

### Larger picture

1.  Does the documentation make sense from a CASA user\'s point of view? Is it complete?
2.  Has all information that is relevant been ported from the inline and online help (for tasks/tools) and CASA Cookbook (for chapters) to the plone page?
3.  If you are reading a task/tool page, are the examples relevant? Should there be more (or fewer) examples? Please make suggestions if you think something is missing.
4.  If you are reading a chapter, is the balance correct between the information found in the chapter text and that found linked in the relevant tasks and tools? Please make suggestions if you think something is missing. 
