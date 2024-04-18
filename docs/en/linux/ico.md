---
layout: page
title: linux/ico (English)
description: "Display an animation of a polyhedron."
content_hash: 29cc6bc9e8cf436e436ee9b81850f8f1ea29bceb
last_modified_at: 2024-04-18
tldri18n_status: 2
---
# ico

Display an animation of a polyhedron.
More information: <https://manned.org/ico.1>.

- Display the wireframe of an icosahedron that changes its position every 0.1 seconds:

`ico -sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>

- Display a solid icosahedron with red faces on a blue background:

`ico -faces -noedges -colors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red</span>` -bg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blue</span>

- Display the wireframe of a cube with size 100x100 that moves by +1+2 per frame:

`ico -obj `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cube</span>` -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100x100</span>` -delta `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+1+2</span>

- Display the inverted wireframe of an icosahedron with line width 10 using 5 threads:

`ico -i -lw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` -threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
