from shapefile import Reader

def extract_regions(shapefile, skip_inds):
    """ Extracts the required polygon for each region.
        A list of indicies is to be provided for regions which should be skipped. """
    regions = {}
    with Reader(shapefile) as reader:
        for idx, shp in enumerate(reader.shapeRecords()):
            if idx not in skip_inds:
                regions[idx] = {}
                regions[idx]['polygon'] = shp.__geo_interface__['geometry']
    return regions


def get_shapefiles():
    shapefile = "./shapes/Admin_Boundaries_-_Environment_Agency_and_Natural_England_Public_Face_Areas.shp"
    skip_indices = list(range(0, 9)) # Removes all coastal boundaries
    skip_indices.append(23)
    return extract_regions(shapefile, skip_indices)

def get_shapefiles_ukcp():
    shapefile = "./ukcp18-uk-land-region-hires/ukcp18-uk-land-region-hires.shp"
    skip_indices = [3]
    return extract_regions(shapefile, skip_indices)