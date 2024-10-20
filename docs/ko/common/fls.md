---
layout: page
title: common/fls (한국어)
description: "이미지 파일이나 장치의 파일과 디렉터리를 나열."
content_hash: 8d526df4dce5ba58c210bf0963eaf00890d439c8
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/fls.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fls.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fls

이미지 파일이나 장치의 파일과 디렉터리를 나열.
더 많은 정보: <https://wiki.sleuthkit.org/index.php?title=Fls>.

- 장치에 대한 재귀 fls 목록을 작성하면, 출력 경로가 C로 시작:

`fls -r -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/loop1p1</span>

- 단일 파티션을 분석하여 이미지에서 파일 시스템이 시작되는 섹터 오프셋을 제공:

`fls -r -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sector</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지_파일</span>

- 단일 파티션을 분석하여, 원래 시스템의 시간대를 제공:

`fls -r -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">timezone</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/loop1p1</span>
