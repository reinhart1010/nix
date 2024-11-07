---
layout: page
title: common/plesk (한국어)
description: "Plesk 호스팅 제어 패널."
content_hash: 7c690260546a65fe995345f18e66237271b8ffcf
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/plesk.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/plesk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># plesk

Plesk 호스팅 제어 패널.
더 많은 정보: <https://docs.plesk.com>.

- 관리자 사용자에 대한 자동 로그인 링크 생성 및 출력:

`plesk login`

- 제품 버전 정보 표시:

`plesk version`

- 호스팅된 모든 도메인 나열:

`plesk bin domain --list`

- `panel.log` 파일에서 변경 사항 감시 시작:

`plesk log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">panel.log</span>

- 대화형 MySQL 콘솔 시작:

`plesk db`

- 기본 편집기로 Plesk 메인 구성 파일 열기:

`plesk conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">panel.ini</span>
