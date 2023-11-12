---
layout: page
title: common/banner (English)
description: "Print the given argument as a large ASCII art."
content_hash: 02076fc82f19598af7e2051c8585e3cba6db3642
last_modified_at: 2023-11-12
related_topics:
  - title: हिन्दी version
    url: /hi/common/banner.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/banner.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/banner.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/banner.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/banner.html
    icon: bi bi-globe
tldri18n_status: 2
---
# banner

Print the given argument as a large ASCII art.
More information: <https://manned.org/banner>.

- Print the text message as a large banner (quotes are optional):

`banner "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`"`

- Print the text message as a banner with a width of 50 characters:

`banner -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`"`

- Read text from `stdin`:

`banner`
