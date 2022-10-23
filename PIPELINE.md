# PIPELINE TECHNICAL CHARACTERISTICS


## Data Collection
* Provider: Sentinelhub
* Raw data:
    * 4 Spectral bands from Sentinel-2-L2A
    * Sentiel SC (Scene Classification: Clouds, shadows, deserts, etc. )
    * 10 m / pixel resolution
    * 512x512 pixel geonormalized tiles, in a mosaic covering the whole of the catalan coast.
    * Aprox file size: XXXX mB
    * Frequency: every 5 days

## Data processing
* Combination of known and propietray algortihms:
    * Land | Water delineation:
        * Use scene classification to separate land from water
        * Use NWDI algorithm as a second source of water\land classification
        * Hybrid approach for better precision. 
    * Near shore bathimetry:
        * [Citar paper] Algorithm for near shore bathymetry (accurate up to -10 m).
    * Outputs:
        * Ortonormalized pixel output of our algorithms (Similar file size as raw data)
        * KMZ/GeoJSON polygonal line:
            * Coastline (depth 0)
            * Near shore contour lines up to a depth of 10 m (with 1 meter precision.)
            * File size: XXX kB
* Compute: On company servers
* Time from data availability (satellite pass) to publication:
est. 10 min

## Results publication:
* All computed and raw data is accessible from a direct download link. Notifciations will be periodically send as soon as new data is available. 
* Historic KMZ data will be accessible via an API
    * The computed results can be embedded in any GIS tools and and currently existing viewers. 

