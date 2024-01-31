---
layout: page
title: osx/defaults (English)
description: "Read and write macOS user configuration for applications."
content_hash: 16548f54061cc6c526c9393e52cbdcbaab433cad
last_modified_at: 2024-01-31
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/osx/defaults.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/defaults.html
    icon: bi bi-globe
tldri18n_status: 2
---
# defaults

Read and write macOS user configuration for applications.
More information: <https://keith.github.io/xcode-man-pages/defaults.1.html>.

- Read system defaults for an application option:

`defaults read "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option</span>`"`

- Read default values for an application option:

`defaults read -app "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option</span>`"`

- Search for a keyword in domain names, keys, and values:

`defaults find "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>`"`

- Write the default value of an application option:

`defaults write "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Speed up Mission Control animations:

`defaults write com.apple.Dock expose-animation-duration -float 0.1`

- Delete all defaults of an application:

`defaults delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application</span>`"`
