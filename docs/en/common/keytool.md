---
layout: page
title: common/keytool (English)
description: "Keytool is a certificate management utility included with Java."
content_hash: 13a8f306f864b565b406776f58284f707d439483
last_modified_at: 2023-06-14
---
# keytool

Keytool is a certificate management utility included with Java.
More information: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/keytool.html>.

- Create a keystore:

`keytool -genkeypair -v -keystore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.keystore</span>` -alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>

- Change a keystore password:

`keytool -storepasswd -keystore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.keystore</span>

- Change a key's password inside a specific keystore:

`keytool -keypasswd -alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` -keystore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.keystore</span>
