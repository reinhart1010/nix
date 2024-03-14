---
layout: page
title: common/datashader_cli (English)
description: "Quick visualization of large datasets using CLI based on datashader."
content_hash: 35027c25b57f0f961711b0c79b6bda8a44338d17
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# datashader_cli

Quick visualization of large datasets using CLI based on datashader.
More information: <https://github.com/wybert/datashader-cli>.

- Create a shaded scatter plot of points and save it to a PNG file and set the background color:

`datashader_cli points `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.parquet</span>` --x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pickup_x</span>` --y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pickup_y</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.png</span>` --background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">black|white|#rrggbb</span>

- Visualize the geospatial data (supports Geoparquet, shapefile, geojson, geopackage, etc.):

`datashader_cli points `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_data.geo.parquet</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_data.png</span>` --geo true`

- Use matplotlib to render the image:

`datashader_cli points `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_data.geo.parquet</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_data.png</span>` --geo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` --matplotlib true`
