#!/usr/bin/env python

import numpy
import pylab
import sys
import mesh.patch as patch

# plot an output file using the solver's dovis script

def makeplot(myd, solverName):

    exec 'import ' + solverName + ' as solver'

    solver.dovis(myd, 0)


if __name__== "__main__":

    print sys.argv

    solver = sys.argv[1]
    file = sys.argv[2]

    myg, myd = patch.read(file)

    makeplot(myd, solver)




