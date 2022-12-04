---
layout: page
title: common/ajson (English)
description: "Executes JSONPath on JSON objects."
content_hash: a4b505842ebff252501ad3c2ff202488a71f7a14
last_modified_at: 2022-12-04
related_topics:
  - title: français version
    url: /fr/common/ajson.html
    icon: bi bi-globe
---
# ajson

Executes JSONPath on JSON objects.
More information: <https://github.com/spyzhov/ajson>.

- Read JSON from a file and execute a specified JSONPath expression:

`ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$..json[?(@.path)]</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.json</span>

- Read JSON from `stdin` and execute a specified JSONPath expression:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.json</span>` | ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$..json[?(@.path)]</span>`'`

- Read JSON from a URL and evaluate a specified JSONPath expression:

`ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">avg($..price)</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/api/</span>`'`

- Read some simple JSON and calculate a value:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>`' | ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2 * pi * $</span>`'`
