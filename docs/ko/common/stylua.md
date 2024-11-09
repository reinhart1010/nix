---
layout: page
title: common/stylua (한국어)
description: "고정된 스타일의 Lua 코드 포매터."
content_hash: 0c17e35cd52ea79b174b5c7e0ddbe96c35929823
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/stylua.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/stylua.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># stylua

고정된 스타일의 Lua 코드 포매터.
더 많은 정보: <https://github.com/JohnnyMorganz/StyLua>.

- 파일이나 전체 디렉토리를 자동으로 포맷:

`stylua `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 특정 파일이 포맷되었는지 확인:

`stylua --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 구성 파일로 실행:

`stylua --config-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `stdin`에서 코드를 포맷하고 `stdout`으로 출력:

`stylua - < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.lua</span>

- 공백을 사용하고 단일 인용부호를 선호하여 파일이나 디렉토리 포맷:

`stylua --indent-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Spaces</span>` --quote-style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AutoPreferSingle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>
