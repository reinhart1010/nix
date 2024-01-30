---
layout: page
title: common/stl2gts (English)
description: "Convert STL files into the GTS (GNU triangulated surface library) file format."
content_hash: ed9fd20fe3f211255670ebf11443060f30c29870
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# stl2gts

Convert STL files into the GTS (GNU triangulated surface library) file format.
More information: <https://manned.org/stl2gts>.

- Convert an STL file to a GTS file:

`stl2gts < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.stl</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.gts</span>

- Convert an STL file to a GTS file and revert face normals:

`stl2gts --revert < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.stl</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.gts</span>

- Convert an STL file to a GTS file and do not merge vertices:

`stl2gts --nomerge < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.stl</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.gts</span>

- Convert an STL file to a GTS file and display surface statistics:

`stl2gts --verbose < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.stl</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.gts</span>

- Display help:

`stl2gts --help`
