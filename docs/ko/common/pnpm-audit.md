---
layout: page
title: common/pnpm-audit (한국어)
description: "프로젝트 의존성을 스캔합니다."
content_hash: f9d485b0cebf4150fccc119acb1d242be212cd9b
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pnpm-audit.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pnpm-audit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pnpm audit

프로젝트 의존성을 스캔합니다.
설치된 패키지에서 알려진 보안 문제를 확인합니다.
더 많은 정보: <https://pnpm.io/cli/audit>.

- 프로젝트의 취약점 식별:

`pnpm audit`

- 취약점 자동 수정:

`pnpm audit fix`

- JSON 형식의 보안 보고서 생성:

`pnpm audit --json > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/audit-report.json</span>

- [D]ev 의존성만 감사:

`pnpm audit --dev`

- [P]roduction 의존성만 감사:

`pnpm audit --prod`

- 선택적 의존성을 감사에서 제외:

`pnpm audit --no-optional`

- 감사 과정에서 레지스트리 오류 무시:

`pnpm audit --ignore-registry-errors`

- 심각도별로 자문 필터링 (low, moderate, high, critical):

`pnpm audit --audit-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">심각도</span>
