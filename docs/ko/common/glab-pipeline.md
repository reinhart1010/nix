---
layout: page
title: common/glab-pipeline (한국어)
description: "GitLab CI/CD 파이프라인을 나열, 보고, 실행."
content_hash: 16ec4dc6cc4442b7e98ced0ce1796924d1cfd1ea
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/glab-pipeline.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/glab-pipeline.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># glab pipeline

GitLab CI/CD 파이프라인을 나열, 보고, 실행.
더 많은 정보: <https://glab.readthedocs.io/en/latest/pipeline>.

- 현재 브랜치에서 실행 중인 파이프라인을 보기:

`glab pipeline status`

- 특정 분기에서 실행 중인 파이프라인을 보기:

`glab pipeline status --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 파이프라인 목록을 가져옴:

`glab pipeline list`

- 현재 브랜치에서 수동 파이프라인을 실행:

`glab pipeline run`

- 특정 브랜치에서 수동 파이프라인을 실행:

`glab pipeline run --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>
