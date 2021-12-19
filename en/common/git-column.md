---
layout: page
title: common/git-column (English)
description: "Display data in columns."
content_hash: 76de5a0647d717c1595c218b227b814332f615a4
---
# git column

Display data in columns.
More information: <https://git-scm.com/docs/git-column>.

- Format the standard input as multiple columns:

`ls | git column --mode=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">column</span>

- Format the standard input as multiple columns with a maximum width of `100`:

`ls | git column --mode=column --width=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Format the standard input as multiple columns with a maximum padding of `30`:

`ls | git column --mode=column --padding=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>
