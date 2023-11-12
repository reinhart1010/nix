---
layout: page
title: common/diffstat (English)
description: "Create a histogram from the output of the `diff` command."
content_hash: 0acf97eceb096be0a32f85b05beb3d7a718191c2
last_modified_at: 2023-11-12
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

`diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>` | diffstat`

- Display inserted, deleted and modified changes as a table:

`diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>` | diffstat -t`
