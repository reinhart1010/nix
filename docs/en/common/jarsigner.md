---
layout: page
title: common/jarsigner (English)
description: "Sign and verify Java archive (JAR) files."
content_hash: 63afb3f3519b6736e3d7da07394c4012a97f5c93
last_modified_at: 2023-06-04
related_topics:
  - title: 中文 version
    url: /zh/common/jarsigner.html
    icon: bi bi-globe
---
# jarsigner

Sign and verify Java archive (JAR) files.
More information: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/jarsigner.html>.

- Sign a JAR file:

`jarsigner `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keystore_alias</span>

- Sign a JAR file with a specific algorithm:

`jarsigner -sigalg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algorithm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keystore_alias</span>

- Verify the signature of a JAR file:

`jarsigner -verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jar</span>
