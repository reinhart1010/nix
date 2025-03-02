---
layout: page
title: common/stty (한국어)
description: "터미널 장치 인터페이스의 옵션 설정."
content_hash: 275e22b4dd47cd64f4258e9352c586965fbb7fe9
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/stty.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/stty.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/stty.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/stty.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/stty.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># stty

터미널 장치 인터페이스의 옵션 설정.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/stty-invocation.html>.

- 현재 터미널의 모든 설정 표시:

`stty --all`

- 행 또는 열의 수 설정:

`stty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rows|cols</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수</span>

- 장치의 실제 전송 속도 확인:

`stty --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/장치_파일</span>` speed`

- 현재 터미널의 모든 모드를 적절한 값으로 재설정:

`stty sane`
