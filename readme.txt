1. Introduction

This directory contains pre-generated Jargo datasets. A Jargo "dataset"
consists of three files: the road network (*.rnet) file, the g-tree for the
road network (*.gtree), and the problem instance (*.instance) file. Datasets
are organized by road network. Top-level directories contain the *.rnet file,
an *.edges file, and a figure of the network. They also contain problems/ and
solutions/ subdirectories.

IMPORTANT: g-trees are not provided due to filesize. You can obtain a g-tree
using the C++ gtree-builder program (https://github.com/jamjpan/GTree) or
by sending me an email and I will send you the g-tree.

Road Statistics:

    Road        G-tree   #edges #vertices
    =====================================
    Beijing:    295 MB  743,822   351,290
    Chengdu:     25 MB   73,854    33,609
    Manhattan:   11 MB   31,444    12,320
    Chengdu(sm): 17 KB      104        46

Problem Statistics:

    Problem  #vehls. #custs.     Ref MIN(re) MAX(re)
    =================================================
    bj5-1      5,000  17,467    1800      +0   +1800
    cd1-1      5,000   8,922    1800      +0   +1800
    cd1-2      5,000 265,056    0700      +0  +61148
    mny-1      5,000   5,033    1800      +0   +1800
    mny-2      5,000   7,012    0045      +0   +1800
    mny-3      5,000  13,986    2330      +0   +3600
    mny-4      5,000  22,168    2330      +0   +7200
    mny-5      5,000 428,017    0100      +0 +172799
    cd0-1          2       4    0000      +0     +15

    *`Ref` is the clock reference time, in military time; `MIN(re)` is the
     smallest customer early time; `MAX(re)` is the largest customer early
     time. Both MIN and MAX are expressed as seconds after Ref. See next
     section for data format definition.

2. Data Formats

  2.1 Problems

  Each *.instance file contains three header rows followed by data rows. The
  first header row lists the *.rnet and *.gtree files to be used with the
  instance. The second header row list the number of vehicles, number of
  customers, and the clock reference time, in military time. The third row lists
  the column headers. The ORIGIN and DEST columns correspond to vertices in the
  *.rnet file. The Q column is the load (positive for customers, negative for
  vehicles). The EARLY and LATE form the time window and are in seconds relative
  to the reference time.

  2.2 Road Networks

  An *.rnet file is a space-delimited file listing all the edges in a road
  network, along with coordinates of the vertices. The first column is the
  edge identifier. The second and third columns are the 'from' and 'to'
  vertices of the edge. The fourth and fifth columns are the longitude
  (x-coordinate) and latitude (y-coordinate) of the 'from' vertex. The sixth
  and seventh columns are the longitude and latitude of the 'to' vertex.

  Vertex '0' is recognized by Jargo as an imaginary vertex. Any edge formed
  using vertex 0 has no distance. The coordinates for vertex 0 are (0, 0).

  An *.edges file is provided listing each edge and its weight. This file is
  used only for building a g-tree. Take care that the vertices in the *.edges
  file are 0-indexed while the vertices in the *.rnet file are 1-indexed.
  You can use the C++ gtree-builder program (https://github.com/jamjpan/GTree)
  to build a g-tree.

