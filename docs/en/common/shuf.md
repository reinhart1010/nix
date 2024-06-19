---
layout: page
title: common/shuf (English)
description: "Generate random permutations."
content_hash: cc7f60992e94c2829974cc9ba17c42952e2685e8
last_modified_at: 2024-06-19
related_topics:
  - title: Nederlands version
    url: /nl/common/shuf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shuf

Generate random permutations.
More information: <https://www.gnu.org/software/coreutils/shuf>.

- Randomize the order of lines in a file and output the result:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Only output the first 5 entries of the result:

`shuf --head-count=5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Write the output to another file:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Generate 3 random numbers in the range 1-10 (inclusive):

`shuf --head-count=3 --input-range=1-10 --repeat`
