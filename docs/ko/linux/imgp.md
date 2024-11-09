---
layout: page
title: linux/imgp (한국어)
description: "JPEG 및 PNG 이미지를 위한 커맨드라인 이미지 리사이저 및 회전기."
content_hash: a5bd456ff9b395152607529571d871b44ec40651
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/imgp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/imgp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># imgp

JPEG 및 PNG 이미지를 위한 커맨드라인 이미지 리사이저 및 회전기.
더 많은 정보: <https://github.com/jarun/imgp>.

- 단일 이미지 및/또는 유효한 이미지 형식을 포함한 전체 폴더 변환:

`imgp -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1366x1000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 이미지를 75% 비율로 조정하고 원본 이미지를 대상 해상도로 덮어쓰기:

`imgp -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">75</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 이미지를 시계 방향으로 90도 회전:

`imgp -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">90</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
