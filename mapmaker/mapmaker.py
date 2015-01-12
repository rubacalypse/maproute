from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import sys, os

sys.path.append(os.path.realpath('.'))

def main():
  plot_lat_long()


def plot_lat_long(coord):
  lat = coord[1].lat
  long = coord[1].long
 
  '''
  m = Basemap(projection='merc', lat_0=lat, lon_0=long+1,\
              llcrnrlat=lat-2,urcrnrlat=lat+2,\
              llcrnrlon=long+2,urcrnrlon=long-2, resolution='h')
  '''
  m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,\
            llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')
  m.drawcoastlines()
  m.fillcontinents(color='coral',lake_color='aqua')

# draw parallels and meridians.
  m.drawparallels(np.arange(-90.,91.,30.))
  m.drawmeridians(np.arange(-180.,181.,60.))
  xpt, ypt =  m(long, lat)
  m.plot(xpt, ypt, 'bo')
  lonlat = 51.53; lonlon = 0.08
  m.drawgreatcircle(long,lat,lonlon,lonlat,linewidth=2,color='b')
  m.drawmapboundary(fill_color='aqua')
  plt.title("Blorp")
  plt.show()


if __name__ == '__main__':
  main()
