---
layout: page
title: common/osv-scanner (English)
description: "Scan various mediums for dependencies and matches them against the OSV database."
content_hash: ba9eb06afeaf95229af4f5e969b0551ccc9b0687
last_modified_at: 2023-02-07
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># osv-scanner

Scan various mediums for dependencies and matches them against the OSV database.
More information: <https://osv.dev/about>.

- Scan a docker image:

`osv-scanner -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker_image_name</span>

- Scan a package lockfile:

`osv-scanner -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/lockfile</span>

- Scan an SBOM file:

`osv-scanner -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/sbom_file</span>

- Scan multiple directories recursively:

`osv-scanner -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory1 directory2 ...</span>

- Skip scanning git repositories:

`osv-scanner --skip-git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|-D</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>

- Output result in JSON format:

`osv-scanner --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-D|-L|-S|-r</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>
