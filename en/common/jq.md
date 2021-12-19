---
layout: page
title: common/jq (English)
description: "A command-line JSON processor that uses a domain-specific language."
content_hash: 593e4ff9020b230016cf8be5c836feadd019952b
---
# jq

A command-line JSON processor that uses a domain-specific language.
More information: <https://stedolan.github.io/jq>.

- Output a JSON file, in pretty-print format:

`jq . `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>

- Output all elements from arrays (or all the values from objects) in a JSON file:

`jq '.[]' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>

- Read JSON objects from a file into an array, and output it (inverse of `jq .[]`):

`jq --slurp . `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>

- Output the first element in a JSON file:

`jq '.[0]' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>

- Output the value of a given key of each element in a JSON text from stdin:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>` | jq 'map(.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>`)'`

- Output the value of multiple keys as a new JSON object (assuming the input JSON has the keys `key_name` and `other_key_name`):

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>` | jq '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{my_new_key</span>`: .`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>`, `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_other_key</span>`: .`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">other_key_name</span>`}'`

- Combine multiple filters:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>` | jq 'unique | sort | reverse'`

- Output the value of a given key to a string (and disable JSON output):

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>` | jq --raw-output '"some text: \(.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>`)"'`
