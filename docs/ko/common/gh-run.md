---
layout: page
title: common/gh-run (한국어)
description: "최근 GitHub Actions 워크플로 실행을 보고, 실행하고, 모니터링."
content_hash: 79f86ac574415cfea1a8bca369afc77a0597a5ae
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/gh-run.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gh run

최근 GitHub Actions 워크플로 실행을 보고, 실행하고, 모니터링.
더 많은 정보: <https://cli.github.com/manual/gh_run>.

- 실행을 인터랙티브하게 선택하여 작업 정보 보기:

`gh run view`

- 특정 실행에 대한 정보 표시:

`gh run view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workflow_run_number</span>

- 작업의 단계에 대한 정보 표시:

`gh run view --job=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_number</span>

- 작업의 로그 표시:

`gh run view --job=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_number</span>` --log`

- 특정 워크플로를 확인하고 실행이 실패한 경우 0이 아닌 상태로 종료:

`gh run view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workflow_run_number</span>` --exit-status && `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "run pending or passed"</span>

- 활성 실행을 인터랙티브하게 선택하고 완료될 때까지 대기:

`gh run watch`

- 실행의 작업을 표시하고 완료될 때까지 대기:

`gh run watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workflow_run_number</span>

- 특정 워크플로 재실행:

`gh run rerun `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workflow_run_number</span>
