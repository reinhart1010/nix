---
layout: page
title: windows/assoc (한국어)
description: "파일 확장자와 파일 유형 간의 연결을 표시하거나 변경."
content_hash: 8318e3846b30af5062545f40322bc17e27cd28c9
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/assoc.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/assoc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/assoc.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/assoc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/assoc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# assoc

파일 확장자와 파일 유형 간의 연결을 표시하거나 변경.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/assoc>.

- 파일 확장자와 파일 유형 간의 모든 연결 나열:

`assoc`

- 특정 확장자의 연결된 파일 유형 표시:

`assoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.txt</span>

- 특정 확장자의 연결된 파일 유형 설정:

`assoc .`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txt</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txtfile</span>

- `assoc`의 출력을 한 화면씩 보기:

`assoc | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">more</span>
