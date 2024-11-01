---
layout: page
title: common/ykman-fido (한국어)
description: "YubiKey FIDO 애플리케이션 관리."
content_hash: c1356c73645832189336c377af8ccbe1dcb6cd98
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/ykman-fido.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ykman-fido.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ykman-fido.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ykman fido

YubiKey FIDO 애플리케이션 관리.
더 많은 정보: <https://docs.yubico.com/software/yubikey/tools/ykman/FIDO_Commands.html>.

- FIDO2 애플리케이션에 대한 일반 정보 표시:

`ykman fido info`

- FIDO PIN 변경:

`ykman fido access change-pin`

- YubiKey에 저장된 거주 인증서 나열:

`ykman fido credentials list`

- YubiKey에서 거주 인증서 삭제:

`ykman fido credentials delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- YubiKey에 저장된 지문 나열 (지문 센서가 있는 키 필요):

`ykman fido fingerprints list`

- YubiKey에 새 지문 추가:

`ykman fido fingerprints add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- YubiKey에서 지문 삭제:

`ykman fido fingerprints delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 모든 FIDO 자격 증명 삭제 (PIN 재시도 횟수를 초과한 후 수행해야 함):

`ykman fido reset`
