<div align="center">

# Rapid Watershed Delineation using an Automatic Outlet Relocation Algorithm

Delineating a large number of watersheds for hydrological simulations in the big data era 🚀⚡🔥<br>
Click on [<kbd>Download</kbd>](https://github.com/xiejx5/watershed_delineation/releases) to start delineation.

</div>
<br>

<div align="center">

![](https://github.com/xiejx5/watershed_delineation/blob/resources/demo.mp4)

</div>
<br>


## 🚀&nbsp;&nbsp;Usage


### How to Get Started
- First, download watershed.zip from the [release page](https://github.com/xiejx5/watershed_delineation/releases)
- Next, unzip and open watershed.exe, clip start to execute an example
<br>


### Inputs
1. Flow direction: the path of [tiff format](https://gdal.org/drivers/raster/gtiff.html#) files, which can be a file path or a folder path (see [example_flowdir.tif](example_flowdir.tif) for example)
2. The given coordinates of watershed outlets: a excel sheet contains longitudes and latitudes in the WGS84 projection. Watershed area is optional as auxiliary information to improve the delineation accuracy (see [example_station.xlsx](example_station.xlsx) for example)
<br>


### Outputs
1. Shapefile: watershed boundaries stored as vector data
2. Info.xlsx: delineated watershed areas, containing areas of confluence, mainstream, and tributray relocations.
3. Map.html: a visual map of watershed boundaries with satellite images as the background
<br>


## Best Practices

<details>
<summary><b>Divide [HydroSHES] or [MERIT] Hydro flow direction into several parts to reduce memorary usage</b></summary>

Use miniconda for your python environments (it's usually unnecessary to install full anaconda environment, miniconda should be enough).
It makes it easier to install some dependencies, like cudatoolkit for GPU support.<br>
Example installation:
```yaml
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```
Create environment using bash script provided in the template:
```yaml
bash bash/setup_conda.sh
```

</details>
