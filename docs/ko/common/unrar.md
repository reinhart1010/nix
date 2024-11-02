---
layout: page
title: common/unrar (한국어)
description: "RAR 압축 파일을 추출."
content_hash: 678050cd9df5f636b7f8ae2963a11c2731577cac
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/unrar.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/unrar.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/unrar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unrar

RAR 압축 파일을 추출.
더 많은 정보: <https://manned.org/unrar>.

- 원본 디렉토리 구조로 파일 추출:

`unrar x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">압축파일.rar</span>

- 지정된 경로에 원본 디렉토리 구조로 파일 추출:

`unrar x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">압축파일.rar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/추출</span>

- 현재 디렉토리에 디렉토리 구조를 무시하고 파일 추출:

`unrar e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">압축파일.rar</span>

- 압축 파일 내 각 파일의 무결성 검사:

`unrar t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">압축파일.rar</span>

- 압축 해제 없이 압축 파일 내의 파일 목록 표시:

`unrar l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">압축파일.rar</span>
