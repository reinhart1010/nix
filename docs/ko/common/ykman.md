---
layout: page
title: common/ykman (한국어)
description: "YubiKey Manager - YubiKey 구성 도구."
content_hash: 11139473ffeab6653b8c679303e7b0ca4db18460
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/ykman.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ykman.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ykman.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ykman

YubiKey Manager - YubiKey 구성 도구.
여러 개의 YubiKey가 연결된 경우, 하위 명령어 앞에 `--device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">serial_number</span>를 추가해야 합니다.
더 많은 정보: <https://docs.yubico.com/software/yubikey/tools/ykman/index.html>.

- YubiKey에 대한 일반 정보 표시 (일련번호, 펌웨어 버전, 기능 등):

`ykman info`

- 연결된 YubiKey를 짧고 한 줄로 설명 (일련번호 포함):

`ykman list`

- 애플리케이션 활성화 및 비활성화에 대한 문서 보기:

`tldr ykman config`

- FIDO 애플리케이션 관리에 대한 문서 보기:

`tldr ykman fido`

- OATH 애플리케이션 관리에 대한 문서 보기:

`tldr ykman oath`

- OpenPGP 애플리케이션 관리에 대한 문서 보기:

`tldr ykman openpgp`
