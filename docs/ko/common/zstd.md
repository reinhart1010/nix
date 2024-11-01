---
layout: page
title: common/zstd (한국어)
description: "Zstandard 압축을 사용하여 파일을 압축하거나 압축 해제."
content_hash: 90ff6d61e331a051cfe48eedad5cfd0fb3dac635
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/zstd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/zstd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/zstd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zstd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zstd

Zstandard 압축을 사용하여 파일을 압축하거나 압축 해제.
더 많은 정보: <https://github.com/facebook/zstd>.

- 파일을 `.zst` 확장자로 새 파일로 압축:

`zstd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일 압축 해제:

`zstd --decompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.zst</span>

- `stdout`으로 압축 해제:

`zstd --decompress --stdout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.zst</span>

- 압축 수준을 지정하여 파일 압축 (1=가장 빠름, 19=가장 느림, 3=기본):

`zstd -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수준</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 더 많은 메모리를 사용하여 더 높은 압축 수준(최대 22) 잠금 해제 (압축 및 압축 해제 모두):

`zstd --ultra -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수준</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
