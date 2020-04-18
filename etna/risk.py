#!/usr/bin/env python

import grass.script as gscript


def main():

    gscript.run_command('g.region', overwrite=True, res='20', w='478000', e='528300', n='4190000', s='4141900', flags='p')
    gscript.run_command('r.import', input='D:/Dokumente_D/Uni/5_Semester/GIS_Proseminar/project/fossgis_project/etna/hazard/QL3MontiRossi.asc', output='hazard', overwrite=True, extent='region')
    #gscript.run_command('r.null', overwrite=True, map='hazard@PERMANENT', null='0')
    gscript.run_command('r.recode', input='hazard@PERMANENT', output='hazard_recoded', rules='D:/Dokumente_D/Uni/5_Semester/GIS_Proseminar/project/fossgis_project/etna/recode_hazard.txt', overwrite=True)
    gscript.run_command('r.reclass', input='hazard_recoded@PERMANENT', output='hazard_reclassified', rules='D:/Dokumente_D/Uni/5_Semester/GIS_Proseminar/project/fossgis_project/etna/reclassification_hazard.txt', overwrite=True)
    gscript.run_command('r.recode', input='vulnerability@PERMANENT', output='vulnerability_recoded', rules='D:/Dokumente_D/Uni/5_Semester/GIS_Proseminar/project/fossgis_project/etna/recode_vulnerability.txt', overwrite=True)

    #risk calculation
    gscript.run_command('r.mapcalc', expression='risk = (vulnerability_recoded@PERMANENT)*(hazard_reclassified@PERMANENT)', overwrite=True)
    gscript.run_command('r.null', overwrite=True, map='risk@PERMANENT', setnull='0')
    #export as picture
    gscript.run_command('r.out.gdal', input='risk', output='D:/Dokumente_D/Uni/5_Semester/GIS_Proseminar/project/fossgis_project/etna/risk.tif', overwrite=True)

if __name__ == '__main__':
    main()
