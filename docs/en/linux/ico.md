---
layout: page
title: linux/ico (English)
description: "Displays an animation of a polyhedron."
content_hash: 08b2b4c67671b20b3f8a3beaa188080f808658ef
last_modified_at: 2023-10-11
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ico

Displays an animation of a polyhedron.
More information: <https://manned.org/ico.1>.

- Display the wireframe of an icosahedron that changes its position every 0.1 seconds:

`ico -sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>

- Display a solid icosahedron with red faces on a blue background:

`ico -faces -noedges -colors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red</span>` -bg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blue</span>

- Display the wireframe of a cube with size 100x100 that moves by +1+2 per frame:

`ico -obj `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cube</span>` -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100x100</span>` -delta `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+1+2</span>

- Display the inverted wireframe of an icosahedron with line width 10 using 5 threads:

`ico -i -lw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` -threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
