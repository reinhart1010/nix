---
layout: page
title: linux/zbarcam (한국어)
description: "비디오 장치에서 바코드(및 QR 코드)를 스캔하고 디코딩."
content_hash: 535bc9e98f4bcaa11fcef906733c6701e639f991
last_modified_at: 2024-10-28
related_topics:
  - title: English version
    url: /en/linux/zbarcam.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/zbarcam.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zbarcam

비디오 장치에서 바코드(및 QR 코드)를 스캔하고 디코딩.
더 많은 정보: <https://manned.org/zbarcam>.

- 바코드를 지속적으로 읽고 `stdout`에 출력:

`zbarcam`

- 스캔하는 동안 출력 비디오 창 비활성화:

`zbarcam --nodisplay`

- 유형 정보 없이 바코드 출력:

`zbarcam --raw`

- 캡처 장치 지정:

`zbarcam `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/비디오_장치</span>
