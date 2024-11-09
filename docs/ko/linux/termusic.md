---
layout: page
title: linux/termusic (한국어)
description: "Rust로 작성된 터미널 음악 플레이어로, vim과 유사한 키 바인딩을 사용합니다."
content_hash: e5b73583a6c41b8c5e352b98658683b37c1db437
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/termusic.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/termusic.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># termusic

Rust로 작성된 터미널 음악 플레이어로, vim과 유사한 키 바인딩을 사용합니다.
같이 보기: `cmus`, `ncmpcpp`, `audacious`.
더 많은 정보: <https://github.com/tramhao/termusic>.

- 특정 폴더로 termusic 열기 (`~/.config/termusic/config.toml`에서 영구적으로 설정 가능):

`termusic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 특정 음악 파일의 앨범 커버 표시 비활성화:

`termusic -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/음악_파일</span>

- 도움말 표시:

`termusic --help`
