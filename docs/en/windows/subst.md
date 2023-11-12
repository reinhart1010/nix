---
layout: page
title: windows/subst (English)
description: "Associates a path with a virtual drive letter."
content_hash: 9cd390652d53ee44636f02ff487f98d055224b48
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/windows/subst.html
    icon: bi bi-globe
tldri18n_status: 2
---
# subst

Associates a path with a virtual drive letter.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/subst>.

- List active associations:

`subst`

- Add an association:

`subst `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Z:</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\Python2.7</span>

- Remove an association:

`subst `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Z:</span>` /d`
