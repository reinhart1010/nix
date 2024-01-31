---
layout: page
title: osx/codesign (English)
description: "Create and manipulate code signatures for macOS."
content_hash: 340d8c98c87e82ff70545284dbf1a8d2c740e4c9
last_modified_at: 2024-01-31
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/osx/codesign.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/codesign.html
    icon: bi bi-globe
tldri18n_status: 2
---
# codesign

Create and manipulate code signatures for macOS.
More information: <https://keith.github.io/xcode-man-pages/codesign.1.html>.

- Sign an application with a certificate:

`codesign --sign "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">My Company Name</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/application_file.app</span>

- Verify the certificate of an application:

`codesign --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/application_file.app</span>
