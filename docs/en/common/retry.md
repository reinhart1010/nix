---
layout: page
title: common/retry (English)
description: "Repeat command until it succeeds or a criterion is met."
content_hash: 5a64c33f1e9aa4f1df90799343159608e719c941
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# retry

Repeat command until it succeeds or a criterion is met.
More information: <https://github.com/minfrin/retry>.

- Retry a command until it succeeds:

`retry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Retry a command every n seconds until it succeeds:

`retry --delay=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Give up after n attempts:

`retry --times=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
