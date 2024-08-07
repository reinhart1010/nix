---
layout: page
title: common/fdupes (English)
description: "Finds duplicate files in a set of directories."
content_hash: 9af0b72e11d0e49e94b0128240175ee5d6c53c40
last_modified_at: 2024-07-21
related_topics:
  - title: français version
    url: /fr/common/fdupes.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fdupes

Finds duplicate files in a set of directories.
More information: <https://github.com/adrianlopezroche/fdupes>.

- Search a single directory:

`fdupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Search multiple directories:

`fdupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory2</span>

- Search a directory recursively:

`fdupes -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Search multiple directories, one recursively:

`fdupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory1</span>` -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory2</span>

- Search recursively, considering hardlinks as duplicates:

`fdupes -rH `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Search recursively for duplicates and display interactive prompt to pick which ones to keep, deleting the others:

`fdupes -rd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Search recursively and delete duplicates without prompting:

`fdupes -rdN `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
