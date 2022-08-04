---
layout: page
title: osx/oathtool (English)
description: "OATH one-time password tool."
content_hash: b058e5dc763ad840f34748a1828c65853de915d4
related_topics:
  - title: 中文 version
    url: /zh/osx/oathtool.html
    icon: bi bi-globe
---
# oathtool

OATH one-time password tool.

- Generate TOTP token (behaves like Google Authenticator):

`oathtool --totp --base32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret</span>

- Generate a TOTP token for a specific time:

`oathtool --totp --now `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2004-02-29 16:21:42</span>` --base32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret</span>

- Validate a TOTP token:

`oathtool --totp --base32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>
