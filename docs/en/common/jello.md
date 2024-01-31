---
layout: page
title: common/jello (English)
description: "A command-line JSON processor using Python syntax."
content_hash: d2f440fc7f8114ad84e08befa5d86058eb3426c7
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# jello

A command-line JSON processor using Python syntax.
More information: <https://github.com/kellyjonbrazil/jello>.

- Pretty-print JSON or JSON-Lines data from `stdin` to `stdout`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>` | jello`

- Output a schema of JSON or JSON Lines data from `stdin` to `stdout` (useful for grep):

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>` | jello -s`

- Output all elements from arrays (or all the values from objects) in JSON or JSON-Lines data from `stdin` to `stdout`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>` | jello -l`

- Output the first element in JSON or JSON-Lines data from `stdin` to `stdout`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>` | jello _[0]`

- Output the value of a given key of each element in JSON or JSON-Lines data from `stdin` to `stdout`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>` | jello '[i.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` for i in _]'`

- Output the value of multiple keys as a new JSON object (assuming the input JSON has the keys `key_name1` and `key_name2`):

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>` | jello '{"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key1</span>`": _.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name1</span>`, "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>`": _.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name2}</span>`'`

- Output the value of a given key to a string (and disable JSON output):

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>` | jello -r '"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">some text</span>`: " + _.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>`'`
