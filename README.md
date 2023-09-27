# stactools-pointcloud

Creates a STAC Item based on the header of a pointcloud.

## Dependencies

PDAL

## Installation
```bash
pip install stactools-pointcloud
```

## Usage

```
stac pointcloud create-item [OPTIONS] HREF DST


HREF is the pointcloud file. DST is directory that a STAC Item JSON file
will be created in.

Options:
  -r, --reader TEXT               Override the default PDAL reader.
  -t, --pointcloud-type TEXT      Set the pointcloud type (default: lidar)
  --compute-statistics / --no-compute-statistics
                                  Compute statistics for the pointcloud (could
                                  take a while)
  -p, --providers TEXT            Path to JSON file containing array of
                                  additional providers
  --help                          Show this message and exit.
  -a, --a_srs TEXT                Proj short string for the lat/lon projection used
                                  to compute the bbox / geometry for STAC.
                                      
stactools package for Pointcloud data.

```

## Example

LAZ archive:

```bash
stac pointcloud create-item https://maps1.vcgov.org/LIDAR/LAZ/USGS_LPC_FL_Peninsular_2018_D18_LID2019_241594_E.laz .
```
