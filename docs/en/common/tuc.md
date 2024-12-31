---
layout: page
title: common/tuc (English)
description: "Cut text (or bytes) where a delimiter matches, then keep the desired parts."
content_hash: 1785ba48f2a605e546e3c73e1c8e7214ce74f8ca
last_modified_at: 2024-12-31
tldri18n_status: 2
---
# tuc

Cut text (or bytes) where a delimiter matches, then keep the desired parts.
A more user-friendly and powerful version of `cut` with sensible defaults.
More information: <https://github.com/riquito/tuc>.

- Cut and rearrange fields:

`echo "foo bar baz" | tuc -d '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"> </span>`' -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3,2,1</span>

- Replace the delimiter `space` with an arrow:

`echo "foo bar baz" | tuc -d ' ' -r ' ➡ '`

- Keep a range of fields:

`echo "foo bar    baz" | tuc -d ' ' -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2:</span>

- Cut using regular expressions:

`echo "a,b, c" | tuc -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[, ]+</span>`' -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,3</span>

- Emit JSON output:

`echo "foo bar baz" | tuc -d '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"> </span>`' --json`
