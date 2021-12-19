---
layout: page
title: osx/codesign (English)
description: "Create and manipulate code signatures for macOS."
content_hash: a0f611214404fd75de9698e9f0cd2dbc0c8bdb20
related_topics:
  - title: 中文 version
    url: /zh/osx/codesign.html
    icon: bi bi-globe
---
# codesign

Create and manipulate code signatures for macOS.
More information: <https://www.unix.com/man-page/osx/1/codesign/>.

- Sign an application with a certificate:

`codesign -s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">My Company Name</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/App.app</span>

- Verify the certificate of an application:

`codesign -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/App.app</span>
