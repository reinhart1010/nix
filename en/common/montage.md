---
layout: page
title: common/montage (English)
description: "ImageMagick image montage tool."
content_hash: 5e247d3e56d083f169f34bf4ef094bc277f0e4b2
---
# montage

ImageMagick image montage tool.
Tiles images into a customisable grid.
More information: <https://imagemagick.org/script/montage.php>.

- Tile images into a grid, automatically resizing images larger than the grid cell size:

`montage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image2.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imageN.png</span>` montage.jpg`

- Tile images into a grid, automatically calculating the grid cell size from the largest image:

`montage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image2.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imageN.png</span>` -geometry +0+0 montage.jpg`

- Set the grid cell size and resize images to fit it before tiling:

`montage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image2.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imageN.png</span>` -geometry 640x480+0+0 montage.jpg`

- Limit the number of rows and columns in the grid, causing input images to overflow into multiple output montages:

`montage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image2.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imageN.png</span>` -geometry +0+0 -tile 2x3 montage_%d.jpg`

- Resize and crop images to fill their grid cells before tiling:

`montage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image2.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imageN.png</span>` -geometry +0+0 -resize 640x480^ -gravity center -crop 640x480+0+0 montage.jpg`
