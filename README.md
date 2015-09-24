*There are some less than scientifically rigourous things about this application, but when we're talking about >10 second delays in read/writes.. small variance due to other environmental factors don't really affect the end result*

## filewrite
I was experiencing delayed IO over NFS to storage.

This is a way of timing reads/writes to that storage (and again for a control storage).

There's python to graph the two results, overlayed.

A very messy and unofficial way of tracking storage delays over time!

<img src="http://bioinformatics.erc.monash.edu/home/steve/plot.png"/>

## Operating
Execute the command in `cmd` in 2 different locations
Set up the variables at the bottom of the `py` file to generate a plot of the read/write times
The C program was compiled with gcc for Ubuntu 14 but given how unexotic it is, it should run on anything
