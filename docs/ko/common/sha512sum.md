---
layout: page
title: common/sha512sum (한국어)
description: "SHA512 암호화 체크섬 계산."
content_hash: a0e3bcaeddd675382686cbdd50e97c7c61eb1ed1
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/common/sha512sum.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/sha512sum.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/sha512sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sha512sum.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sha512sum.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sha512sum

SHA512 암호화 체크섬 계산.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- 하나 이상의 파일에 대해 SHA512 체크섬 계산:

`sha512sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- SHA512 체크섬 목록을 파일에 계산하고 저장:

`sha512sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sha512</span>

- `stdin`에서 SHA512 체크섬 계산:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | sha512sum`

- SHA512 체크섬과 파일 이름 목록이 포함된 파일을 읽어 모든 파일이 일치하는지 검증:

`sha512sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sha512</span>

- 누락된 파일 또는 검증 실패 시에만 메시지 표시:

`sha512sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sha512</span>

- 누락된 파일은 무시하고 검증 실패 시에만 메시지 표시:

`sha512sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sha512</span>
