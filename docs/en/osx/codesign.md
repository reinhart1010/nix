---
layout: page
title: osx/codesign (English)
description: "Create and manipulate code signatures for macOS."
content_hash: 935b90d2fef24eeb882a05ada0535d697fa34bad
last_modified_at: 2023-11-12
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
More information: <https://www.unix.com/man-page/osx/1/codesign/>.

- Sign an application with a certificate:

`codesign --sign "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">My Company Name</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/application_file.app</span>

- Verify the certificate of an application:

`codesign --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/application_file.app</span>
