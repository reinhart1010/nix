---
layout: page
title: common/rip (한국어)
description: "파일이나 디렉토리를 무덤에 보내 제거하고, 복구할 수 있도록 합니다."
content_hash: 3a06a1db2c0c1199b89487c87c4272a0e20bd03e
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/rip.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rip.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rip

파일이나 디렉토리를 무덤에 보내 제거하고, 복구할 수 있도록 합니다.
더 많은 정보: <https://github.com/nivekuil/rip>.

- 지정된 위치에서 파일이나 디렉토리를 제거하고 무덤에 보관:

`rip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/다른/파일_또는_디렉토리</span>

- 파일이나 디렉토리를 대화식으로 제거하며, 제거 전마다 확인 메시지를 표시:

`rip --inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/다른/파일_또는_디렉토리</span>

- 현재 디렉토리 내에 원래 있던 파일과 디렉토리를 무덤에서 모두 나열:

`rip --seance`

- 무덤에 있는 모든 파일과 디렉토리를 영구 삭제:

`rip --decompose`

- 가장 최근에 제거된 파일과 디렉토리를 복원:

`rip --unbury`

- `rip --seance`로 나열된 모든 파일과 디렉토리를 복원:

`rip --seance --unbury`
