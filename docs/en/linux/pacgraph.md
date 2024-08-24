---
layout: page
title: linux/pacgraph (English)
description: "Draw a graph of installed packages to PNG/SVG/GUI/console."
content_hash: 30a4f2cf73afa8d17be11547bbf160f77c796997
last_modified_at: 2024-08-24
tldri18n_status: 2
---
# pacgraph

Draw a graph of installed packages to PNG/SVG/GUI/console.
More information: <https://github.com/keenerd/pacgraph>.

- Produce an SVG and PNG graph:

`pacgraph`

- Produce an SVG graph:

`pacgraph --svg`

- Print summary to console:

`pacgraph --console`

- Override the default filename/location (Note: Do not specify the file extension):

`pacgraph --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Change the color of packages that are not dependencies:

`pacgraph --top=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color</span>

- Change the color of package dependencies:

`pacgraph --dep=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color</span>

- Change the background color of a graph:

`pacgraph --background=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color</span>

- Change the color of links between packages:

`pacgraph --link=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color</span>
