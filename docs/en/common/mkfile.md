---
layout: page
title: common/mkfile (English)
description: "Create one or more empty files of any size."
content_hash: ad6b829abab1a33a913a668b9c5451f6998a9d20
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/common/mkfile.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfile

Create one or more empty files of any size.
More information: <https://manned.org/mkfile>.

- Create an empty file of 15 kilobytes:

`mkfile -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15k</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Create a file of a given size and unit (bytes, KB, MB, GB):

`mkfile -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b|k|m|g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Create two files of 4 megabytes each:

`mkfile -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">first_filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">second_filename</span>
