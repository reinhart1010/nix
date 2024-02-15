---
layout: page
title: common/sc_wartsfilter (English)
description: "Select specific records from a `warts` file."
content_hash: 16591ed2d0e57ab8655bc88cab13483765e83f71
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# sc_wartsfilter

Select specific records from a `warts` file.
More information: <https://www.caida.org/catalog/software/scamper/>.

- Filter all data records that had specific destinations and write them to a separate file:

`sc_wartsfilter -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.warts</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.warts</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.5</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.6</span>

- Filter all records that had certain destinations in a prefix and write them to a separate file:

`sc_wartsfilter -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.warts</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.warts</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8::/32</span>

- Filter all records that using a specific action and output them as JSON:

`sc_wartsfilter -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.warts</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ping</span>` | sc_warts2json`
