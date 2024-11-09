---
layout: page
title: linux/fwupdmgr (한국어)
description: "`fwupd`를 사용하여 UEFI를 포함한 장치 펌웨어 업데이트."
content_hash: d340a66e0f79c9f0b9ec84978e1ece89b62e24d2
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/fwupdmgr.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/fwupdmgr.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/fwupdmgr.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fwupdmgr

`fwupd`를 사용하여 UEFI를 포함한 장치 펌웨어 업데이트.
더 많은 정보: <https://fwupd.org/>.

- fwupd에 의해 감지된 모든 장치 표시:

`fwupdmgr get-devices`

- LVFS에서 최신 펌웨어 메타데이터 다운로드:

`fwupdmgr refresh`

- 시스템의 장치에 사용할 수 있는 업데이트 나열:

`fwupdmgr get-updates`

- 펌웨어 업데이트 설치:

`fwupdmgr update`
