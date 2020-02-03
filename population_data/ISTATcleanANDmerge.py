#!/usr/bin/env python

import grass.script as gscript
import os

def main():
    # set working directory -> replace with own wd
    os.chdir('C:/Users/jnlpu/Documents/Studium/Geographie/5. Semester/FOSSGIS/Abschlussprojekt')

    # import adminSicily.geojson located in the wd
    gscript.run_command('v.import', overwrite=True, input='adminSicily.geojson', output='adminSicily')

    # delete everything that is not a polygon:
    # Overpass Turbo can't differentate between polygons, ways and so on itself, so data still needs to be reduced; fortunately the data is sorted by the types relation, ways and nodes and luckily our 390 polygons are the 390 relations listed first; so this simple sql query will remove all other geo-objects
    gscript.run_command('v.db.droprow', overwrite=True, input='adminSicily@ISTATmerge', where='cat > 390', output='adminClean')

    # delete (lots of) unecessary columns (oh dear...)
    gscript.run_command('v.db.dropcolumn', overwrite=True, map='adminClean@ISTATmerge', columns=['admin_level','boundary','name_ar','name_ru','type','wikidata','wikipedia','alt_name_ar','name_cs','name_el','name_de','name_he','name_ko','name_lt','name_nl','name_fr','name_it','name_scn','name_uk','name_zh','name_bg','name_ca','alt_name_la','name_ja','name_la','name_sr','alt_name_scn','old_name','alt_name','name_sq','natural','place','xrelations','image','website','short_name','old_name_el','tourism','leisure','name_en','name_left','name_right','source','natural_1','loc_name','fixme','province_left','province_right','created_by','note','history','city_left','city_right','traffic_sign','description','ele','old_name_ar','short_name_ar','volcano_type','wheelchair','capital','name_be','name_es','name_fa','name_fi','name_kn','name_pl','name_pt','population','alt_name_el','heritage','heritage_operator','name_an','name_pms','name_roa_tara','gfoss_id','short_name_scn','istat_id','old_name_scn','name_mk','old_name_la','name_aae','old_name__1938','population_1593','population_1861','population_1871','population_1881','population_1901','name_eo','name_ka','amenity','cargo','ferry','public_transport','ford','crossing','crossing_ref','highway','distance','railway','bus','mountain_pass','prominence','waterway','harbour','maxdraft','maxlength','phone','volcano_status','seamark_harbour_category','seamark_type','vhf_channel','barrier','surface','email','bicycle','foot','alt_name_cs','addr_city','addr_postcode','addr_street','mooring','seamark_mooring_category','seamark_name','junction','noexit','seamark_information','seamark_small_craft_facility_category','access','material','stile','fee','name_sk','name_sv','ref_whc','whc_criteria','whc_inscription_date','operator','traffic_calming','horse','motorcycle','name_grc','direction'])

    # import the ISTATdata.csv table; excel preparation necessary see below
    # this command does not recognize the suitable data type per column, see the help page for the command; therefore this needs the creation of a textfile named ISTATdata.csvt and the data types wanted
    gscript.run_command('db.in.ogr', overwrite=True, input='ISTATdata.csv', output='ISTATdata')

    # print the table to check for errors
    gscript.run_command('db.select', table='ISTATdata')

    # renaming the 'name' column to avoid redundances
    gscript.run_command('v.db.renamecolumn', map='adminClean@ISTATmerge', column=('name','Intermediary'))

    # merging via the 'name' of 'adminClean' and the 'Name' column of 'ISTATdata
    # ! unfortunately not possible like that, because the python algorithm does not work with characters with an accent grave (even though the program is able to print them), so all these rows are left blank
    # gscript.run_command('v.db.join', map='adminClean@ISTATmerge', column='name', other_table='ISTATdata', other_column='Name')

    # work-around with excel:
    # the 'ref_ISTAT' column of 'adminClean' equals the 'Postal_Code' column of 'ISTATdata' without the first '0'
    # Excel: by creating a new 'ISTATdata' column 'Merger' with ="0"&A2 for E2, ="0"&A3 for E3 and so on one can create a column entirely equaling 'ref_ISTAT'
    gscript.run_command('v.db.join', map='adminClean@ISTATmerge', column='ref_ISTAT', other_table='ISTATdata', other_column='Merger')

    # cleaning out my table
    gscript.run_command('v.db.dropcolumn', overwrite=True, map='adminClean@ISTATmerge', columns=['id','xid','ref_ISTAT','ref_catasto','Name','Merger'])

    # renaming 'Intermediary to 'Name' back again
    gscript.run_command('v.db.renamecolumn', map='adminClean@ISTATmerge', column=('Intermediary','Name'))

    # putting some color into this map: choose one
    #gscript.run_command('v.colors', map='adminClean@ISTATmerge', use='attr', column='Population', color='population')
    gscript.run_command('v.colors', map='adminClean@ISTATmerge', use='attr', column='Population_Density', color='population_dens')

    # exporting the processed map as a .geojson
    gscript.run_command('v.out.ogr', overwrite=True, input='adminClean@ISTATmerge', output='adminFinal.geojson', format='GeoJSON')
if __name__ == '__main__':
    main()
