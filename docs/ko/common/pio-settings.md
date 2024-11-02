---
layout: page
title: common/pio-settings (한국어)
description: "PlatformIO 설정을 보고 수정."
content_hash: c34d430a3810389e57efcd944a6b64231c94ec7a
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pio-settings.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pio-settings.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pio-settings.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pio settings

PlatformIO 설정을 보고 수정.
더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/cmd_settings.html>.

- 모든 PlatformIO 설정의 이름, 값 및 설명 표시:

`pio settings get`

- 특정 PlatformIO 설정의 이름, 값 및 설명 표시:

`pio settings get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설정</span>

- 특정 설정 값을 설정:

`pio settings set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설정</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 모든 수정된 설정 값을 기본값으로 재설정:

`pio settings reset`
