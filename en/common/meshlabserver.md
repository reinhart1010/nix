---
layout: page
title: common/meshlabserver (English)
description: "Command-line interface for the MeshLab 3D mesh processing software."
content_hash: 207c040e81748b9f58dc1a2584f2e058b73b412d
---
# meshlabserver

Command-line interface for the MeshLab 3D mesh processing software.
More information: <https://manned.org/meshlabserver>.

- Convert an STL file to an OBJ file:

`meshlabserver -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.stl</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.obj</span>

- Convert a WRL file to a OFF file, including the vertex and face normals in the output mesh:

`meshlabserver -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.wrl</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.off</span>` -om vn fn`

- Dump a list of all the available processing filters into a file:

`meshlabserver -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Process a 3D file using a filter script created in the MeshLab GUI (Filters > Show current filter script > Save Script):

`meshlabserver -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.ply</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.ply</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filter_script.mlx</span>

- Process a 3D file using a filter script, writing the output of the filters into a log file:

`meshlabserver -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.x3d</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.x3d</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filter_script.mlx</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logfile</span>
