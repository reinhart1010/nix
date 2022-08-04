---
layout: page
title: osx/mkfile (English)
description: "Create one or more empty files of any size."
content_hash: 683205e853a6e89cab40fba23fd57a28618c2b47
related_topics:
  - title: 中文 version
    url: /zh/osx/mkfile.html
    icon: bi bi-globe
---
# mkfile

Create one or more empty files of any size.
More information: <https://ss64.com/osx/mkfile.html>.

- Create an empty file of 15 kilobytes:

`mkfile -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15k</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Create a file of a given size and unit (bytes, KB, MB, GB):

`mkfile -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b|k|m|g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Create two files of 4 megabytes each:

`mkfile -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">first_filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">second_filename</span>
