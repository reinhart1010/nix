---
layout: page
title: common/ar (한국어)
description: "아카이브로부터 생성, 수정, 추출 (`.a`, `.so`, `.o`)."
content_hash: 852161dcff5f65ee40d077ad57d2b657ca17ff29
related_topics:
  - title: English version
    url: /en/common/ar.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ar.html
    icon: bi bi-globe
---
# ar

아카이브로부터 생성, 수정, 추출 (`.a`, `.so`, `.o`).
더 많은 정보: <https://manned.org/ar>.

- 보관소로부터 모든 멤버를 추출하기:

`ar -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">libfoo.a</span>

- 보관소 멤버 리스트 보여주기:

`ar -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">libfoo.a</span>

- 보관소로 파일을 대체하거나 추가하기:

`ar -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">libfoo.a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">baz.o</span>

- object 파일 인덱스 삽입( `ranlib` 와 같은 기능입니다):

`ar -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">libfoo.a</span>

- 파일 및 첨부된 객체 파일 색인을 사용하여 보관소에 작성:

`ar -rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">libfoo.a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">baz.o</span>
