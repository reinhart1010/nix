---
layout: page
title: common/aria2c (한국어)
description: "빠른 다운로드 유틸리티."
content_hash: d39673cc094b427d6aa2420991f4cc987b6d7913
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/aria2c.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aria2c.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aria2c.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/aria2c.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/aria2c.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aria2c.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aria2c

빠른 다운로드 유틸리티.
HTTP(S), FTP, SFTP, BitTorrent, and Metalink를 지원합니다.
더 많은 정보: <https://aria2.github.io>.

- URl을 파일에 다운로드:

`aria2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 다중 소스를 다운로드:

`aria2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_2</span>

- 파일에 나열된 URI 다운로드:

`aria2c -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- 여러 연결로 다운로드:

`aria2c -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">connections_num</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 사용자 이름과 암호가 있는 FTP 다운로드:

`aria2c --ftp-user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --ftp-passwd=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 다운로드 속도를 바이트/s로 제한:

`aria2c --max-download-limit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">speed</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
