---
layout: page
title: common/ykman-oath (한국어)
description: "OATH YubiKey 애플리케이션 관리."
content_hash: 62933c21700057ca8d2d50f1487b7ef9985e6c3b
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/ykman-oath.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ykman-oath.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ykman oath

OATH YubiKey 애플리케이션 관리.
`keyword`는 이름 또는 발행자의 일부일 수 있습니다.
더 많은 정보: <https://docs.yubico.com/software/yubikey/tools/ykman/OATH_Commands.html>.

- OATH 애플리케이션에 대한 일반 정보 표시:

`ykman oath info`

- OATH 계정을 보호하는 데 사용되는 비밀번호 변경 (`--clear`를 추가하여 제거):

`ykman oath access change`

- 새 계정 추가 (`--issuer`는 선택 사항):

`ykman oath accounts add --issuer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">발행자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 모든 계정 나열 (발행자 포함):

`ykman oath accounts list`

- 현재 TOTP/HOTP 코드와 함께 모든 계정 나열 (키워드로 목록 필터링 가능):

`ykman oath accounts code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- 계정 이름 변경:

`ykman oath accounts rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">발행자:이름|이름</span>

- 계정 삭제:

`ykman oath accounts delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- 모든 계정 삭제 및 공장 초기화:

`ykman oath reset`
