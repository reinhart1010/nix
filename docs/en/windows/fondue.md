---
layout: page
title: windows/fondue (English)
description: "A command-line installer for optional Windows features."
content_hash: 8614b6bdee4e967b083c6cee525aefa1c4553a97
related_topics:
  - title: 中文 version
    url: /zh/windows/fondue.html
    icon: bi bi-globe
---
# fondue

A command-line installer for optional Windows features.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/fondue>.

- Enable a specific Windows feature:

`fondue /enable-feature:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature</span>

- Hide all output messages to the user:

`fondue /enable-feature:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature</span>` /hide-ux:all`

- Specify a caller process name for error reporting:

`fondue /enable-feature:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature</span>` /caller-name:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
