---
layout: page
title: common/git-column (English)
description: "Display data in columns."
content_hash: c17812c01378d44d946f3f1a6df66b53f45ece9a
last_modified_at: 2023-08-09
related_topics:
  - title: Türkçe version
    url: /tr/common/git-column.html
    icon: bi bi-globe
---
# git column

Display data in columns.
More information: <https://git-scm.com/docs/git-column>.

- Format `stdin` as multiple columns:

`ls | git column --mode=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">column</span>

- Format `stdin` as multiple columns with a maximum width of `100`:

`ls | git column --mode=column --width=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Format `stdin` as multiple columns with a maximum padding of `30`:

`ls | git column --mode=column --padding=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>
