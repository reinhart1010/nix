---
layout: page
title: common/unar (English)
description: "Extract contents from archive files."
content_hash: 0f6fb72541a479fc8cf7f39df13c8979e3968d12
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/common/unar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unar

Extract contents from archive files.
More information: <https://manned.org/unar>.

- Extract an archive to the current directory:

`unar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive</span>

- Extract an archive to the specified directory:

`unar -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive</span>

- Force overwrite if files to be unpacked already exist:

`unar -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive</span>

- Force rename if files to be unpacked already exist:

`unar -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive</span>

- Force skip if files to be unpacked already exist:

`unar -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive</span>
