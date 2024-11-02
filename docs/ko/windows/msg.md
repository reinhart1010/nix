---
layout: page
title: windows/msg (한국어)
description: "사용자 또는 세션에 메시지 보내기."
content_hash: b9941ffc64fb5ef87c0b041de5cb6932e02b909f
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/windows/msg.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/msg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/msg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/msg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># msg

사용자 또는 세션에 메시지 보내기.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/msg>.

- 특정 사용자 또는 세션에 메시지 보내기:

`msg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명|세션명|세션_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>

- `stdin`에서 메시지 보내기:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`" | msg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명|세션명|세션_아이디</span>

- 특정 서버에 메시지 보내기:

`msg /server:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명|세션명|세션_아이디</span>

- 현재 컴퓨터의 모든 사용자에게 메시지 보내기:

`msg *`

- 메시지 지연 설정 (초):

`msg /time:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>
