---
layout: page
title: common/aria2 (한국어)
description: "경량 멀티 프로토콜 및 멀티 소스 명령줄 다운로드 유틸리티입니다."
content_hash: e0b84a07699d3197725e7dfb69368b3dcb63128b
related_topics:
  - title: bosanski version
    url: /bs/common/aria2.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aria2.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/aria2.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aria2.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aria2.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aria2

경량 멀티 프로토콜 및 멀티 소스 명령줄 다운로드 유틸리티입니다.
HTTP, HTTPS, FTP, SFTP, BitTorrent와 Metalink를 지원합니다.
더 많은 정보: <https://aria2.github.io/>.

- 웹 리소스 다운로드:

`aria2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.org/myLinux.iso</span>

- 멀티 소스 리소스 다운로드:

`aria2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://mirror1.org/myLinux.iso</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://mirror2.org/myLinux.iso</span>

- 호스트당 2개의 연결을 사용하여 다운로드 :

`aria2c -x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.org/myLinux.iso</span>

- Metalink URL로 다운로드:

`aria2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.org/myLinux.metalink</span>

- BitTorrent URI로 다운로드:

`aria2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.org/myLinux.torrent</span>

- BitTorrent Magnet URI로 다운로드:

`aria2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'magnet:?xt=urn:btih:248D0A1CD08284299DE78D5C1ED359BB46717D8C'</span>

- 파일로 URls 다운로드:

`aria2c -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uris.txt</span>
