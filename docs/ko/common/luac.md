---
layout: page
title: common/luac (한국어)
description: "Lua 바이트코드 컴파일러."
content_hash: 82547ecf28e8e9cb4a2621730449c2fa8b11990a
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/luac.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/luac.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># luac

Lua 바이트코드 컴파일러.
더 많은 정보: <https://www.lua.org>.

- Lua 소스 파일을 Lua 바이트코드로 컴파일:

`luac -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">바이트_코드.luac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스.lua</span>

- 출력에 디버그 심볼을 포함하지 않음:

`luac -s -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">바이트_코드.luac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스.lua</span>
