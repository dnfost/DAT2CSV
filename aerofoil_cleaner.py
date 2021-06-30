# Credits to Daniel Foster for base code and idea

# This tool helps convert Selig format dat files to csvs
import csv
import requests
import matplotlib.pyplot as plt


def make_csv(dat: str, coord_z: int = 0) -> str:
    '''
    Turns selig format .dat file into x,y,z coordinates
    of an aerofoil on the xy plane.

    dat: DAT file read as a single string
    coord_z: Z level of the wing (0 by default)

    returns: aerofoil name
    '''
    lines = dat.splitlines()  # Split per line

    aerofoil_name = lines.pop(0)  # Pop first line
    aerofoil_name = ''.join(e for e in aerofoil_name if e.isalnum())
    # Filter names to only include alphanumeric characters (avoid illegal name)

    with open(aerofoil_name + ".csv", 'w', newline='') as file:
        writer = csv.writer(file)  # Init CSV writer

        for row in lines:
            writer.writerow([*row.split(), coord_z])
            # Get the x, y coords, pair them with z

    return aerofoil_name


def get_dat(url: str) -> str:
    '''
    Gets the DAT file given the web url to one.
    '''
    r = requests.get(url)
    return r.text


def plot_aerofoil_by_name(name: str) -> None:
    '''
    Plots processed csv of aerofoil from name of existing csv,
    saves picture to folder
    '''
    with open(name + ".csv", 'r') as f:
        points = f.read().splitlines()
        x = [float(c.split(",")[0]) for c in points]
        y = [float(c.split(",")[1]) for c in points]
        plt.plot(x, y)
        plt.title(name)
        plt.ylim(-0.5, 0.5)
        plt.xlim(0, 1)
        plt.savefig(name)
        plt.show()


def plot_aerofoil_by_url(url: str) -> None:
    '''
    Plots processed csv of aerofoil from url
    '''
    dat = get_dat(url)
    name = make_csv(dat)
    plot_aerofoil_by_name(name)


if __name__ == "__main__":
    url = input("Input the URL of the aerofoil you want on the web.")
    plot_aerofoil_by_url(url)
    # For example https://m-selig.ae.illinois.edu/ads/coord/naca2411.dat
