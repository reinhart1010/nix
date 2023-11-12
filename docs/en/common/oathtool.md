---
layout: page
title: common/oathtool (English)
description: "OATH one-time password tool."
content_hash: 861204430f0a75d148687c49293b06d298560385
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/common/oathtool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# oathtool

OATH one-time password tool.
More information: <https://www.nongnu.org/oath-toolkit/oathtool.1.html>.

- Generate TOTP token (behaves like Google Authenticator):

`oathtool --totp --base32 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret</span>`"`

- Generate a TOTP token for a specific time:

`oathtool --totp --now "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2004-02-29 16:21:42</span>`" --base32 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret</span>`"`

- Validate a TOTP token:

`oathtool --totp --base32 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>`"`
