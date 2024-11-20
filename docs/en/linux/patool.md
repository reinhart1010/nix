---
layout: page
title: linux/patool (English)
description: "Archive file manager."
content_hash: ed9843983c55e9f2a8bdd87b860d76bb1d231da5
last_modified_at: 2024-11-20
tldri18n_status: 2
---
# patool

Archive file manager.
Various archive formats can be created, extracted, tested, listed, searched, repacked, and compared.
More information: <https://github.com/wummel/patool>.

- Extract an archive:

`patool extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive</span>

- List contents of an archive:

`patool list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive</span>

- Compare the contents of two archives and display the differences in the standard output:

`patool diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive2</span>

- Search for a string inside the contents of an archive:

`patool search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive</span>
