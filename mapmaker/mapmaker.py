from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import sys, os
# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners
# of the map.
# lat_ts is the latitude of true scale.
# resolution = 'c' means use crude resolution coastlines.
sys.path.append(os.path.realpath('.'))

def main():
  plot_lat_long()


def plot_lat_long(coord):
  lat = coord[1].lat
  long = coord[1].long
  m = Basemap(projection='merc', lat_0=lat, lon_0=long+1,\
              llcrnrlat=lat-2,urcrnrlat=lat+2,\
              llcrnrlon=long+2,urcrnrlon=long-2, resolution='h')
  
  m.drawcoastlines()
  m.fillcontinents(color='coral',lake_color='aqua')

# draw parallels and meridians.
  m.drawparallels(np.arange(-90.,91.,30.))
  m.drawmeridians(np.arange(-180.,181.,60.))
  xpt, ypt =  m(long, lat)
  m.plot(xpt, ypt, 'bo')
  m.drawmapboundary(fill_color='aqua')
  plt.title("Maproute")
  plt.show()


if __name__ == '__main__':
  main()
