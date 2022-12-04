---
layout: page
title: common/jdupes (English)
description: "A powerful duplicate file finder and an enhanced fork of fdupes."
content_hash: ad92d7dbffb6d7868185824f73f0227179577281
last_modified_at: 2022-12-04
---
# jdupes

A powerful duplicate file finder and an enhanced fork of fdupes.
More information: <https://github.com/jbruchon/jdupes>.

- Search a single directory:

`jdupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Search multiple directories:

`jdupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory2</span>

- Search all directories recursively:

`jdupes --recurse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Search directory recursively and let user choose files to preserve:

`jdupes --delete --recurse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Search multiple directories and follow subdirectores under directory2, not directory1:

`jdupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory1</span>` --recurse: `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory2</span>

- Search multiple directories and keep the directory order in result:

`jdupes -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory3</span>
