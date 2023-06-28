---
layout: page
title: common/sdcv (English)
description: "StarDict, a command-line dictionary client."
content_hash: 5367b9a44224fa7469ba84467d25edfd5f23ea3b
last_modified_at: 2023-06-28
---
# sdcv

StarDict, a command-line dictionary client.
Dictionaries are provided separately from the client.
More information: <https://manned.org/sdcv>.

- Start `sdcv` interactively:

`sdcv`

- List installed dictionaries:

`sdcv --list-dicts`

- Display a definition from a specific dictionary:

`sdcv --use-dict `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dictionary_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Look up a definition with a fuzzy search:

`sdcv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Look up a definition with an exact search:

`sdcv --exact-search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Look up a definition and format the output as JSON:

`sdcv --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Search for dictionaries in a specific directory:

`sdcv --data-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>
