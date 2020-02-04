#!/usr/bin/env python

import grass.script as gscript
import os

def main():
    # set working directory -> replace with own wd
    os.chdir('C:/Users/jnlpu/Documents/Studium/Geographie/5. Semester/FOSSGIS/Abschlussprojekt')

    # set region
    gscript.run_command('g.region', overwrite=True, res='20', w='478000', e='528300', n='4190000', s='4141900', flags='p')

    # import DTM cut to the region
    gscript.run_command('r.import', overwrite=True, input='DTM_Italy_20m_by_Sonny/DTM_Italy_20m.tif', extent='region', output='DTM')

    # export the dtm
    gscript.run_command('r.out.gdal', overwrite=True, input='DTM@PERMANENT', output='DTMsicily.tif', format='GTiff')
if __name__ == '__main__':
    main()
