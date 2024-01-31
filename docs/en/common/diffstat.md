---
layout: page
title: common/diffstat (English)
description: "Create a histogram from the output of the `diff` command."
content_hash: c1ab349419fad61dd6a361796a857f6447bbc7a7
last_modified_at: 2024-01-31
related_topics:
  - title: italiano version
    url: /it/common/diffstat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/diffstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# diffstat

Create a histogram from the output of the `diff` command.
More information: <https://manned.org/diffstat>.

- Display changes in a histogram:

`diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>` | diffstat`

- Display inserted, deleted and modified changes as a table:

`diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>` | diffstat -t`
