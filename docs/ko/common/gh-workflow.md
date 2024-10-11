---
layout: page
title: common/gh-workflow (한국어)
description: "GitHub Actions 워크플로우를 나열, 보기 및 실행."
content_hash: de8d263df47f6350f4fa99ce8d7eb451bc111003
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/gh-workflow.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gh-workflow.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gh workflow

GitHub Actions 워크플로우를 나열, 보기 및 실행.
더 많은 정보: <https://cli.github.com/manual/gh_workflow>.

- 상호작용식으로 워크플로우를 선택하여 최신 작업 보기:

`gh workflow view`

- 기본 브라우저에서 특정 워크플로우 보기:

`gh workflow view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id|workflow_name|filename.yml</span>` --web`

- 특정 워크플로우의 YAML 정의 표시:

`gh workflow view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id|workflow_name|filename.yml</span>` --yaml`

- 특정 Git 브랜치 또는 태그의 YAML 정의 표시:

`gh workflow view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id|workflow_name|filename.yml</span>` --ref `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch|tag_name</span>` --yaml`

- 워크플로우 파일 나열 (`--all`을 사용하여 비활성 워크플로우 포함 가능):

`gh workflow list`

- 매개변수와 함께 수동으로 워크플로우 실행:

`gh workflow run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id|workflow_name|filename.yml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--raw-field param1=value1 --raw-field param2=value2 ...</span>

- 특정 브랜치 또는 태그를 사용하여 `stdin`에서 JSON 매개변수로 수동 워크플로우 실행:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{"param1": "value1", "param2": "value2", ...}</span>`' | gh workflow run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id|workflow_name|filename.yml</span>` --ref `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch|tag_name</span>

- 특정 워크플로우 활성화 또는 비활성화:

`gh workflow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id|workflow_name|filename.yml</span>
