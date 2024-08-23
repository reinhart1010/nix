---
layout: page
title: linux/pacgraph (English)
description: "Draw a graph of installed packages to PNG/SVG/GUI/console."
content_hash: 30a4f2cf73afa8d17be11547bbf160f77c796997
last_modified_at: 2024-08-23
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pacgraph.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pacgraph

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
