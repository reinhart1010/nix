---
layout: page
title: common/dvc-commit (한국어)
description: "프로젝트에서 DVC로 추적되는 파일의 변경 사항 기록."
content_hash: 49e986c399b6e92324942371f4e1a2819f32b57d
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/dvc-commit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dvc commit

프로젝트에서 DVC로 추적되는 파일의 변경 사항 기록.
더 많은 정보: <https://dvc.org/doc/command-reference/commit>.

- 모든 DVC로 추적된 파일과 디렉토리의 변경 사항 커밋:

`dvc commit`

- 지정된 DVC로 추적된 대상의 변경 사항 커밋:

`dvc commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>

- 디렉토리 내의 모든 DVC로 추적된 파일을 재귀적으로 커밋:

`dvc commit --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
