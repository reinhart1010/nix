---
layout: page
title: osx/shuf (English)
description: "Generate random permutations."
content_hash: d0dfc9979798054b5544e0630a9173f3014967fb
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/osx/shuf.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/shuf.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/shuf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shuf

Generate random permutations.
More information: <https://www.unix.com/man-page/linux/1/shuf/>.

- Randomize the order of lines in a file and output the result:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Only output the first 5 entries of the result:

`shuf --head-count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Write output to another file:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_filename</span>

- Generate random numbers in range 1-10:

`shuf --input-range=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-10</span>
