---
layout: page
title: common/osv-scanner (English)
description: "Scan various mediums for dependencies and matches them against the OSV database."
content_hash: 1a9fb2407311f1689b0145aa8f3ee84068e327b4
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# osv-scanner

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

- Skip scanning Git repositories:

`osv-scanner --skip-git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|-D</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>

- Output result in JSON format:

`osv-scanner --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-D|-L|-S|-r</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>
