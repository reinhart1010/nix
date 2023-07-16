---
layout: page
title: windows/fondue (English)
description: "Install optional Windows features."
content_hash: b7784ac41dc371f130e4a966ea6b9bc7592bba61
last_modified_at: 2023-07-16
related_topics:
  - title: 中文 version
    url: /zh/windows/fondue.html
    icon: bi bi-globe
---
# fondue

Install optional Windows features.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/fondue>.

- Enable a specific Windows feature:

`fondue /enable-feature:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature</span>

- Hide all output messages to the user:

`fondue /enable-feature:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature</span>` /hide-ux:all`

- Specify a caller process name for error reporting:

`fondue /enable-feature:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature</span>` /caller-name:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
