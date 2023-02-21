---
layout: page
title: common/keytool (English)
description: "Keytool is a certificate management utility included with Java."
content_hash: 32e5bc21f55835ffef77ed827731ac70b0ed9d46
last_modified_at: 2023-02-21
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># keytool

Keytool is a certificate management utility included with Java.
More information: <https://docs.oracle.com/en/java/javase/19/docs/specs/man/keytool.html>.

- Create a keystore:

`keytool -genkeypair -v -keystore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.keystore</span>` -alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>

- Change a keystore password:

`keytool -storepasswd -keystore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.keystore</span>

- Change a key's password inside a specific keystore:

`keytool -keypasswd  -alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` -keystore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.keystore</span>
