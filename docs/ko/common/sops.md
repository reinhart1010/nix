---
layout: page
title: common/sops (한국어)
description: "SOPS (Secrets OPerationS): 비밀 관리를 위한 간단하고 유연한 도구."
content_hash: 9e57faea63a005adcb9308096f54bcc1bcdf774b
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sops.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sops.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sops

SOPS (Secrets OPerationS): 비밀 관리를 위한 간단하고 유연한 도구.
더 많은 정보: <https://github.com/mozilla/sops>.

- 파일 암호화:

`sops -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.json</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.enc.json</span>

- 파일을 `stdout`으로 복호화:

`sops -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.enc.json</span>

- `sops` 파일에서 선언된 키 업데이트:

`sops updatekeys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.enc.yaml</span>

- `sops` 파일의 데이터 키 회전:

`sops -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.enc.yaml</span>

- 파일 암호화 후 확장자 변경:

`sops -d --input-type json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.enc.json</span>

- 이름으로 키를 추출하고, 번호로 배열 요소 추출:

`sops -d --extract '["an_array"][1]' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.enc.json</span>

- 두 `sops` 파일 간의 차이점 표시:

`diff <(sops -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/secret1.enc.yaml</span>`) <(sops -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/secret2.enc.yaml</span>`)`
