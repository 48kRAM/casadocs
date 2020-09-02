

# Average in split 

Highlights on averaging using split

Time and channel averaging are available within **split** using the *timebin* and *width* parameters. The way that time averaging operates can be further controlled by *combine*, which is a sub-parameter of *timebin.*

The *timebin* parameter gives the averaging interval. It takes a quantity, e.g. *timebin=\'30s\'* for 30-second time averaging.  By default the time-span of time averaging will be limited by scan boundaries, *i.e.* the time average will not be extended to average data from multiple scans together. Similarly, time averaging will by default not extend across state boundaries (states are telescope-specific entities; for ALMA a state corresponds to a sub-scan).  These default limits on time averaging can be modified by setting *combine* to \'*scan\'*, \'*state\'*, or \'*state,scan\'* to ignore one or both types of boundaries and average across them.  *combine* is a sub-parameter of *timebin* which is enabled by selecting a non-zero time averaging interval.

The *width* parameter defines the number of channels to average to form a given output channel. This can be specified globally for all spw, e.g.

```
width = 5
```

or specified per spw, e.g.

```
width = [2,3]
```

to average 2 channels of 1st spectral window selected and 3 in the second one.

<div class="alert alert-warning">
ALERT: When averaging channels **split** will produce negative channel widths (as reported by **listobs**) if frequency goes down with increasing channel number, whether or not the input channel widths are negative. The *band*widths and channel resolutions will still be positive."
</div>
