---
layout: page
title: common/ar (한국어)
description: "아카이브로부터 생성, 수정, 추출 (`.a`, `.so`, `.o`)."
content_hash: dd54721d1ad78dcc6940eb08efed76760416ac69
last_modified_at: 2024-01-13
related_topics:
  - title: English version
    url: /en/common/ar.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ar.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ar.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ar

아카이브로부터 생성, 수정, 추출 (`.a`, `.so`, `.o`).
더 많은 정보: <https://manned.org/ar>.

- 보관소로부터 모든 멤버를 추출하기:

`ar x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.a</span>

- 보관소 멤버 리스트 보여주기:

`ar t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ar</span>

- 보관소로 파일을 대체하거나 추가하기:

`ar r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.deb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/debian-binary 경로/대상/control.tar.gz 경로/대상/data.tar.xz ...</span>

- object 파일 인덱스 삽입( `ranlib` 와 같은 기능입니다):

`ar s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.a</span>

- 파일 및 첨부된 객체 파일 색인을 사용하여 보관소에 작성:

`ar rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.o 경로/대상/파일2.o ...</span>
