---
layout: page
title: common/grumphp (한국어)
description: "소스 코드 품질 검사를 가능하게 하는 PHP Composer 플러그인."
content_hash: ea61376c3d719c890e4f4398e402804ca1fa662e
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/grumphp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/grumphp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># grumphp

소스 코드 품질 검사를 가능하게 하는 PHP Composer 플러그인.
더 많은 정보: <https://github.com/phpro/grumphp>.

- Git 훅을 등록:

`grumphp git:init`

- 사전 커밋 후크를 수동으로 트리거:

`grumphp git:pre-commit`

- 버전이 지정된 모든 파일을 확인:

`grumphp run`
