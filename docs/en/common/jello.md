---
layout: page
title: common/jello (English)
description: "A command-line JSON processor using Python syntax."
content_hash: 59244386a7a01ab1eabdc8b6517cfb6a536caef5
last_modified_at: 2022-12-04
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

- Output the value of multiple keys as a new JSON object (assuming the input JSON has the keys `key_name` and `other_key_name`):

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>` | jello '{"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_new_key</span>`": _.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>`, "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_other_key</span>`": _.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">other_key_name}</span>`'`

- Output the value of a given key to a string (and disable JSON output):

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>` | jello -r '"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">some text</span>`: " + _.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>`'`
