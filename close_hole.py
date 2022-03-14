import os
import glob
import geopandas as gpd
from shapely.geometry import Polygon


def close_holes(poly: Polygon) -> Polygon:
    """
    Close polygon holes by limitation to the exterior ring.
    Args:
        poly: Input shapely Polygon
    Example:
        df.geometry.apply(lambda p: close_holes(p))
    """
    if poly.interiors:
        return Polygon(list(poly.exterior.coords))
    else:
        return poly


if __name__ == '__main__':
    files = glob.glob('./*.shp')
    for f_in in files:
        f_out = os.path.splitext(os.path.basename(f_in))[0] + '_closed.shp'
        gdf = gpd.read_file(f_in, encoding='gbk')
        gdf.geometry = gdf.geometry.apply(lambda p: close_holes(p))
        gdf.to_file(f_out, encoding='gbk')

        # uncomment to export as .kml format
        # from osgeo import gdal
        # f_out_kml = os.path.splitext(os.path.basename(f_in))[0] + '_closed.kml'
        # ds_kml = gdal.VectorTranslate(destNameOrDestDS=f_out_kml,
        #                               srcDS=f_out, format='KML')
        # ds_kml = None
