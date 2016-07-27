# Introduction

The IR manager needs to import 201 dissertations into DSpace from the following quarters

- 2015.08 Summer
- 2015.12 Autumn
- 2016.03 Winter
- 2016.06 Spring

The 201 dissertations that need to be imported will have the Creative Commons license in the following XML element from the XML metadata that comes with every disseration

- DISS_creative_commons_license
    - DISS_abbreviation

In order to successfully import each disseration into DSpace they must conform to Simple Archive Format (SAF) which is described in the DSpace documentation page [here](https://wiki.duraspace.org/display/DSDOC5x/Importing+and+Exporting+Items+via+Simple+Archive+Format)

There is a tool available for creating SAF items available at [SAFBuilder Github page](https://github.com/DSpace-Labs/SAFBuilder)

# Results of Experimentation

There are 255 dissertations total with something inside the DISS_abbreviation element. The options are

- CC-BY
- CC-BY-NC
- CC-BY-NC-ND
- CC-BY-NC-SA
- none

In addition to DISS_abbreviation, it has been relayed by the IR manager that there may be an additional field to check in.

However, the options for this field appear to be 

- 1
- 0
- empty element

For the fields that have something in DISS_abbreviation and something in the DISS_acceptance element, there does not appear to be any relation between 0 1 and whether the abbreviation text is some varation of CC or none

A given record may have none in the abbreviation element and a 1 or a 0 in the acceptance element.

A given record may also have some variation of CC in the abbreviation element and a 1 or a 0 in the acceptance field.

