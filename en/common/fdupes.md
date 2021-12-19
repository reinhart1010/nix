---
layout: page
title: common/fdupes (English)
description: "Finds duplicate files in a given set of directories."
content_hash: 0b7ed0c3892024fa6fe52f2a728d73aca4ee68c2
related_topics:
  - title: français version
    url: /fr/common/fdupes.html
    icon: bi bi-globe
---
# fdupes

Finds duplicate files in a given set of directories.
More information: <https://github.com/adrianlopezroche/fdupes>.

- Search a single directory:

`fdupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory</span>

- Search multiple directories:

`fdupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory2</span>

- Search a directory recursively:

`fdupes -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory</span>

- Search multiple directories, one recursively:

`fdupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory1</span>` -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory2</span>

- Search recursively for duplicates and display interactive prompt to pick which ones to keep, deleting the others:

`fdupes -rd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory</span>

- Search recursively and delete duplicates without prompting:

`fdupes -rdN `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory</span>
