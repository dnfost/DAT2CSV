import csv

def make_csv(coords):

    aerofoil_name = ""
    coord_x = []
    coord_y_old = []
    coord_y = []
    coord_z = "0"

    for char in coords:

        if char == "\n":
            break

        else:
            aerofoil_name = aerofoil_name + char

    aerofoil_name = ''.join(e for e in aerofoil_name if e.isalnum())

    filename = aerofoil_name + ".csv"

    with open(filename, 'w', newline='') as file:

        writer = csv.writer(file)
        
        coords = coords.split(" ")
        coords = list(filter(('').__ne__, coords))

        index = 0

        while coords[index][-1] != "\n":

            coords.remove(coords[0])

        coords.remove(coords[0])

        for index in range(0, len(coords)):

            if index % 2 == 0:

                coord_x.append(coords[index])

            else:

                coord_y_old.append(coords[index])

        for element in coord_y_old:

            for char in element:

                if char == "\n":

                    element = element.replace("\n", "")
                    coord_y.append(element)

                elif "\n" not in element:

                    coord_y.append(element)

        for index in range(0, len(coord_x)):

            writer.writerow([coord_x[index], coord_y[index], coord_z])

if __name__ == "__main__":

    coords = """SC(2)-0714 Supercritical airfoil (coordinates from Raymer w/ one correction)
  1.000000 -0.010400
  0.990000 -0.007100
  0.980000 -0.003900
  0.970000 -0.000900
  0.950000  0.004900
  0.920000  0.013100
  0.900000  0.018100
  0.870000  0.025100
  0.850000  0.029400
  0.820000  0.035300
  0.800000  0.038900
  0.770000  0.043900
  0.750000  0.046900
  0.720000  0.050900
  0.700000  0.053300
  0.680000  0.055500
  0.650000  0.058500
  0.620000  0.061000
  0.600000  0.062500
  0.570000  0.064500
  0.550000  0.065600
  0.530000  0.066600
  0.500000  0.067800
  0.480000  0.068400
  0.450000  0.069200
  0.430000  0.069500
  0.400000  0.069700
  0.380000  0.069800
  0.350000  0.069600
  0.330000  0.069200
  0.300000  0.068500
  0.270000  0.067300
  0.250000  0.066400
  0.220000  0.064600
  0.200000  0.063200
  0.170000  0.060600
  0.150000  0.058500
  0.120000  0.054800
  0.100000  0.051800
  0.070000  0.046200
  0.050000  0.041100
  0.040000  0.038100
  0.030000  0.034300
  0.020000  0.029300
  0.010000  0.021900
  0.005000  0.015800
  0.002000  0.009500
  0.000000  0.000000
  0.002000 -0.009300
  0.005000 -0.016000
  0.010000 -0.022100
  0.020000 -0.029500
  0.030000 -0.034400
  0.040000 -0.038100
  0.050000 -0.041200
  0.070000 -0.046200
  0.100000 -0.051700
  0.120000 -0.054700
  0.150000 -0.058500
  0.170000 -0.060600
  0.200000 -0.063300
  0.220000 -0.064700
  0.250000 -0.066600
  0.280000 -0.068000
  0.300000 -0.068700
  0.320000 -0.069200
  0.350000 -0.069600
  0.370000 -0.069600
  0.400000 -0.069200
  0.420000 -0.068800
  0.450000 -0.067600
  0.480000 -0.065700
  0.500000 -0.064400
  0.530000 -0.061400
  0.550000 -0.058800
  0.580000 -0.054300
  0.600000 -0.050900
  0.630000 -0.045100
  0.650000 -0.041000
  0.680000 -0.034600
  0.700000 -0.030200
  0.730000 -0.023500
  0.750000 -0.019200
  0.770000 -0.015000
  0.800000 -0.009300
  0.830000 -0.004800
  0.850000 -0.002400
  0.870000 -0.001300
  0.890000 -0.000800
  0.920000 -0.001600
  0.940000 -0.003500
  0.950000 -0.004900
  0.960000 -0.006600
  0.970000 -0.008500
  0.980000 -0.010900
  0.990000 -0.013700
  1.000000 -0.016300"""

    make_csv(coords)