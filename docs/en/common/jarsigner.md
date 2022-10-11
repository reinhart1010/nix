---
layout: page
title: common/jarsigner (English)
description: "Sign and verify Java archive (JAR) files."
content_hash: 3d0630c95e009c17157283ba3d27d962a2898ff5
related_topics:
  - title: 中文 version
    url: /zh/common/jarsigner.html
    icon: bi bi-globe
---
# jarsigner

Sign and verify Java archive (JAR) files.
More information: <https://docs.oracle.com/javase/9/tools/jarsigner.htm>.

- Sign a JAR file:

`jarsigner `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keystore_alias</span>

- Sign a JAR file with a specific algorithm:

`jarsigner -sigalg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algorithm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keystore_alias</span>

- Verify the signature of a JAR file:

`jarsigner -verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jar</span>
