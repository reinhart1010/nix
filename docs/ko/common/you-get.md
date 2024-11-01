---
layout: page
title: common/you-get (한국어)
description: "웹에서 미디어 콘텐츠(비디오, 오디오, 이미지)를 다운로드."
content_hash: 378aa38b6d632ead45e4ac9d654fdc0d865c5482
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/you-get.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/you-get.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/you-get.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># you-get

웹에서 미디어 콘텐츠(비디오, 오디오, 이미지)를 다운로드.
같이 보기: `yt-dlp`, `youtube-viewer`, `instaloader`.
더 많은 정보: <https://you-get.org>.

- 웹의 특정 미디어에 대한 정보 출력:

`you-get --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/video?id=value</span>

- 특정 URL에서 미디어 다운로드:

`you-get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/video?id=value</span>

- Google Videos에서 검색 및 다운로드:

`you-get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- 특정 위치에 미디어 다운로드:

`you-get --output-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --output-filename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/watch?v=value</span>

- 프록시를 사용하여 미디어 다운로드:

`you-get --http-proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프록시_서버</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/watch?v=value</span>
