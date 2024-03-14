---
layout: page
title: common/osv-scanner (English)
description: "Scan various mediums for dependencies and matches them against the OSV database."
content_hash: 7168265eea010d5b0756b280241254b320ec286d
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# osv-scanner

Scan various mediums for dependencies and matches them against the OSV database.
More information: <https://osv.dev/about>.

- Scan a Docker image:

`osv-scanner -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker_image_name</span>

- Scan a package lockfile:

`osv-scanner -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/lockfile</span>

- Scan an SBOM file:

`osv-scanner -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/sbom_file</span>

- Scan multiple directories recursively:

`osv-scanner -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory1 directory2 ...</span>

- Skip scanning Git repositories:

`osv-scanner --skip-git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|-D</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>

- Output result in JSON format:

`osv-scanner --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-D|-L|-S|-r</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>
