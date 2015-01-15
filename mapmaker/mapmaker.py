from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import sys, os

sys.path.append(os.path.realpath('.'))

def main():
  plot_lat_long()


def plot_lat_long(coords):
  
  starting_lat = coords[0][1].lat
  starting_lon = coords[0][1].long
  print "starting lat: %s\nstarting lon: %s\n" % (starting_lat, starting_lon)
  for coord in coords[1:]:
    lat = coord[1].lat
    lon = coord[1].long
    print "lat: %s\nlon: %s\n" % (lat, lon)
    m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,\
              llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')
    m.drawcoastlines()
    m.fillcontinents(color='coral',lake_color='aqua')

# draw parallels and meridians.
    m.drawparallels(np.arange(-90.,91.,30.))
    m.drawmeridians(np.arange(-180.,181.,60.))
    xpt, ypt =  m(lon, lat)
    m.plot(xpt, ypt, 'bo')
    lonlat = 51.53; lonlon = 0.08
    m.drawgreatcircle(starting_lon,starting_lat,lon,lat,linewidth=2,color='b')
    m.drawmapboundary(fill_color='aqua')
    plt.title("Blorp")
    plt.show()
    starting_lat = lat
    starting_lon = lon

if __name__ == '__main__':
  main()
