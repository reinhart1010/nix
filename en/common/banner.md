---
layout: page
title: common/banner (English)
description: "Print the given argument as a large ASCII art."
content_hash: 78748087d10fa231b5fa9bb061ea07d5f23ab69d
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
  - title: 中文 version
    url: /zh/common/banner.html
    icon: bi bi-globe
---
# banner

Print the given argument as a large ASCII art.
More information: <https://man.archlinux.org/man/banner.1>.

- Print the text message as a large banner (quotes are optional):

`banner "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`"`

- Print the text message as a banner with a width of 50 characters:

`banner -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`"`

- Read text from stdin:

`banner`
