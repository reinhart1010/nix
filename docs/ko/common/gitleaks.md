---
layout: page
title: common/gitleaks (한국어)
description: "Git 레포지토리에서 유출된 비밀 및 API 키를 탐지."
content_hash: 373fb43d4383eb3b50b838389ef8b05d1ced7c58
last_modified_at: 2024-10-23
related_topics:
  - title: English version
    url: /en/common/gitleaks.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/gitleaks.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gitleaks.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gitleaks

Git 레포지토리에서 유출된 비밀 및 API 키를 탐지.
더 많은 정보: <https://github.com/gitleaks/gitleaks>.

- 원격 디렉터리 스캔:

`gitleaks detect --repo-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://github.com/username/repository.git</span>

- 로컬 디렉터리 스캔:

`gitleaks detect --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 스캔 결과를 JSON 파일로 출력:

`gitleaks detect --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>` --report `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/리포트.json</span>

- 사용자 정의 규칙 파일을 사용:

`gitleaks detect --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>` --config-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성파일.toml</span>

- 특정 커밋에서 스캔을 시작:

`gitleaks detect --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>` --log-opts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--since=commit_id</span>

- 커밋 전에 커밋되지 않은 변경사항을 검색:

`gitleaks protect --staged`

- 스캔 중에 보안 위험 노출로 식별된 부분을 나타내는 자세한 출력을 표시:

`gitleaks protect --staged --verbose`
