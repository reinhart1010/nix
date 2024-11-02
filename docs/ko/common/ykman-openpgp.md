---
layout: page
title: common/ykman-openpgp (한국어)
description: "OpenPGP YubiKey 애플리케이션 관리."
content_hash: 084a1eb35424772430f906e03528547fc4c1dba7
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/ykman-openpgp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ykman-openpgp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ykman openpgp

OpenPGP YubiKey 애플리케이션 관리.
참고: 일부 설정을 위해 `gpg --card-edit`를 사용해야 합니다.
더 많은 정보: <https://docs.yubico.com/software/yubikey/tools/ykman/OpenPGP_Commands.html>.

- OpenPGP 애플리케이션에 대한 일반 정보 표시:

`ykman openpgp info`

- 사용자 PIN, 재설정 코드 및 관리자 PIN의 재시도 횟수 설정:

`ykman openpgp access set-retries `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- 사용자 PIN, 재설정 코드 또는 관리자 PIN 변경:

`ykman openpgp access change-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pin|reset-code|admin-pin</span>

- OpenPGP 애플리케이션 초기화 (관리자 PIN 재시도 횟수를 초과한 후 수행해야 합니다):

`ykman openpgp reset`
