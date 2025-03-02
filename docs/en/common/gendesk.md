---
layout: page
title: common/gendesk (English)
description: "Specifies the command to generate a `.desktop` file and a download icon with minimal information."
content_hash: 87030ce44c23ed9c5d113cf20c8818346276b49c
last_modified_at: 2025-03-02
related_topics:
  - title: 中文 version
    url: /zh/common/gendesk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gendesk

Specifies the command to generate a `.desktop` file and a download icon with minimal information.
More information: <https://gendesk.roboticoverlords.org>.

- Create a `.desktop` file named `app`:

`gendesk -n --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app</span>`" --exec "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/app</span>`" --icon "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/icon.png</span>`" --comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">This is application</span>`"`

- Create a `.desktop` file named `app`, do not display any output, and overwrite it if it exists:

`gendesk -q -f -n --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app</span>`" --exec "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/app</span>`" --icon "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/icon.png</span>`" --comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">This is application</span>`"`

- Display help:

`gendesk -h`
