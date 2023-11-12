---
layout: page
title: common/fakedata (English)
description: "Generate fake data using a large variety of generators."
content_hash: 445f506d945c553347f2ace861894eae496dd2c3
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# fakedata

Generate fake data using a large variety of generators.
More information: <https://github.com/lucapette/fakedata>.

- List all valid generators:

`fakedata --generators`

- Generate data using one or more generators:

`fakedata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">generator1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">generator2</span>

- Generate data with a specific output format:

`fakedata --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">csv|tab|sql</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">generator</span>

- Generate a given number of data items (defaults to 10):

`fakedata --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">generator</span>

- Generate data using a custom output template (the first letter of generator names must be capitalized):

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\{\{Generator\}\}</span>`" | fakedata`
