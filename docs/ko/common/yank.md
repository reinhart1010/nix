---
layout: page
title: common/yank (한국어)
description: "`stdin`에서 입력을 읽고 선택 인터페이스를 표시하여 필드를 선택하고 클립보드에 복사할 수 있게 합니다."
content_hash: 6158127163e588daf954e45db9dc80432135ac92
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/yank.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/yank.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yank

`stdin`에서 입력을 읽고 선택 인터페이스를 표시하여 필드를 선택하고 클립보드에 복사할 수 있게 합니다.
더 많은 정보: <https://manned.org/yank>.

- 기본 구분자 (\f, \n, \r, \s, \t)를 사용하여 Yank:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sudo dmesg</span>` | yank`

- 전체 라인을 Yank:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sudo dmesg</span>` | yank -l`

- 특정 구분자를 사용하여 Yank:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo hello=world</span>` | yank -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">=</span>

- 특정 패턴과 일치하는 필드만 Yank:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ps ux</span>` | yank -g "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[0-9]+</span>`"`
