---
layout: page
title: common/jwt (English)
description: "Work with JSON Web Tokens (JWTs)."
content_hash: eb53156e5214955b3d717a0d516419f1c5172560
last_modified_at: 2023-07-16
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/jwt.html
    icon: bi bi-globe
---
# jwt

Work with JSON Web Tokens (JWTs).
Encryption algorithms available are HS256, HS384, HS512, RS256, RS384, RS512, ES256, ES384.
More information: <https://github.com/mike-engel/jwt-cli>.

- Decode a JWT:

`jwt decode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jwt_string</span>

- Decode a JWT as a JSON string:

`jwt decode -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jwt_string</span>

- Encode a JSON string to a JWT:

`jwt encode --alg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HS256</span>` --secret `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234567890</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json_string</span>`'`

- Encode key pair payload to JWT:

`jwt encode --alg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HS256</span>` --secret `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234567890</span>` -P key=value`
