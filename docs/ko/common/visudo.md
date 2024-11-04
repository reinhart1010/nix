---
layout: page
title: common/visudo (한국어)
description: "sudoers 파일을 안전하게 편집."
content_hash: 9551b0ee4a35412d62411670e5e005a8650e8ee4
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/visudo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/visudo.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/visudo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# visudo

sudoers 파일을 안전하게 편집.
더 많은 정보: <https://www.sudo.ws/docs/man/visudo.man>.

- sudoers 파일 편집:

`sudo visudo`

- sudoers 파일 오류 검사:

`sudo visudo -c`

- 특정 편집기를 사용하여 sudoers 파일 편집:

`sudo EDITOR=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">편집기</span>` visudo`

- 버전 정보 표시:

`visudo --version`
