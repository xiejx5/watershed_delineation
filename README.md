<div align="center">

# Rapid Watershed Delineation<br>using an Automatic Outlet Relocation Algorithm

Delineating a large number of watersheds for hydrological simulations in the big data era 🔥<br>

</div>
<br>

<div align="center">

https://user-images.githubusercontent.com/29588684/131083101-51bce671-66a7-462a-99de-67f6912d42e5.mp4

</div>
<br>


## 🚀&nbsp;&nbsp;Usage


### How to Get Started
- First, download watershed.zip from the [release page](https://github.com/xiejx5/watershed_delineation/releases)
- Next, unzip and open watershed.exe, clip start to execute an example
<br>


### Inputs
1. Flow direction: a file path or a folder path of tiff (see [example_flowdir.tif](example_flowdir.tif) for example)
2. The given coordinates of watershed outlets: a excel sheet contains longitudes and latitudes in the WGS84 projection. Watershed area is optional as auxiliary information to improve the delineation accuracy (see [example_station.xlsx](example_station.xlsx) for example)
<br>


### Outputs
1. Shapefile: watershed boundaries stored as vector data
2. Info.xlsx: delineated watershed areas, containing areas of confluence, mainstream, and tributray relocations.
3. Map.html: a visual map of watershed boundaries with satellite images as the background
<br>


## ⚡&nbsp;&nbsp;Best Practices

### Use flow directions of [HydroSHEDS](https://www.hydrosheds.org/) and [MERIT Hydro](http://hydro.iis.u-tokyo.ac.jp/~yamadai/MERIT_Hydro/)
HydroSHEDS and MERIT Hydro are 90m-resolution flow directions with pits removed. They have been confirmed effective in watershed delineation. It is recommended to divide the global flow directions into several parts to reduce memory usage.
<br>

### Rerun the algorithm with watershed area as auxiliary information
Suppose the algorithm incorrectly relocates a outlet to the tributray during the first run, and the correct relocation should be on the mainstream. Since the algoirthm also returns watershed area relocated on mainstream, we can quickly use the watershed area as auxiliary information to correct the relocation to the mainstream.