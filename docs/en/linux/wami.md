---
layout: page
title: linux/wami (English)
description: "An open-source and easy-to-use tool that recommends suitable programs for tasks."
content_hash: e88f54b55d5895c8619ab8b2d95e89565662bcf3
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# wami

An open-source and easy-to-use tool that recommends suitable programs for tasks.
More information: <https://github.com/evait-security/wami>.

- Find expanded results in all categories from the lake and [S]ort them in the specified order:

`wami --show-all -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">asc|desc</span>` --search-all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>

- Search GitHub to find expanded results, [S]orted in descending order:

`wami --show-all -S desc --github `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>

- Search GitHub for topics that match the search string:

`wami --list-topics `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>

- Search the lake for a tool used in pentests to query for default credentials and [S]ort the results in descending order:

`wami -S desc --search-all pentest credential default`
