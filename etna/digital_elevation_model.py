#!/usr/bin/env python
# short code with some possible preparation processes for a typical DTM or DEM
# each of these steps should only be processed if necessary! Some processes may affect the performance of Q-Lavha.

import grass.script as gscript
import os

def main():
    # set working directory -> replace with own wd

    os.chdir('C:/Users/jnlpu/Documents/Studium/Geographie/5. Semester/FOSSGIS/Abschlussprojekt')



    # set region (region used for the vulnerability analysis)

    gscript.run_command('g.region', overwrite=True, res='20', w='478000', e='528300', n='4190000', s='4141900', flags='p')



    # import DTM cut to the region 
    # apart from the possibility of the extent being too huge or too small for proper processing, the exact extent is irrelevant!

    gscript.run_command('r.import', overwrite=True, input='NameofDTMorDEM.tif', extent='region', output='DTM')



    # create map without depression for q-lavha (only if necesarry in the specific case; see Q-Lavha Manual)

    gscript.run_command('r.fill.dir', overwrite=True, input='DTM@PERMANENT', output='DTMoutput', direction='DTMdirection')


    # doing it again to make sure it's without depression (again, only if necessary)

    gscript.run_command('r.fill.dir', overwrite=True, input='DTMoutput@PERMANENT', output='DTMoutput', direction='DTMdirection')



    # export the dtm

    gscript.run_command('r.out.gdal', overwrite=True, input='DTMoutput@PERMANENT', output='NameOutputDTM.tif', format='GTiff')
if __name__ == '__main__':
    main()
