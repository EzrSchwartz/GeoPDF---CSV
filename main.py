from osgeo import ogr, gdal
import os


def convert_geopdf_to_csv(geopdf_path, csv_path):
    # Enable GDAL/OGR exceptions
    gdal.UseExceptions()

    # Register drivers
    gdal.AllRegister()

    # Open the GeoPDF
    ds = gdal.OpenEx(geopdf_path, gdal.OF_VECTOR)
    if ds is None:
        print("Could not open the GeoPDF file.")
        return

    # Get the first layer
    layer = ds.GetLayerByIndex(0)
    if layer is None:
        print("Could not get the first layer from the GeoPDF.")
        return

    # Open CSV file for writing
    with open(csv_path, 'w') as csv_file:
        # Write CSV headers
        field_names = [field.name for field in layer.schema]
        csv_file.write(','.join(field_names) + '\n')

        # Write feature attributes to CSV
        for feature in layer:
            attributes = [str(feature.GetField(field)) for field in field_names]
            csv_file.write(','.join(attributes) + '\n')

    print(f"GeoPDF data has been converted to CSV at {csv_path}")


# Example usage
geopdf_path = r"C:\Users\ezran\Downloads\CT_Westport_20210305_TM_geo.pdf"
csv_path = r"C:\Users\ezran\PycharmProjects\geopdftocsv\geodata.csv"
convert_geopdf_to_csv(geopdf_path, csv_path)
