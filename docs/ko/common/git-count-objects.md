---
layout: page
title: common/git-count-objects (한국어)
description: "풀리지 않은 객체의 수와 디스크 사용량을 계산."
content_hash: e217b44becedde6401cb87091b28fac338db9b0a
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-count-objects.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-count-objects.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-count-objects.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git count-objects

풀리지 않은 객체의 수와 디스크 사용량을 계산.
더 많은 정보: <https://git-scm.com/docs/git-count-objects>.

- 모든 객체를 계산하고 총 디스크 사용량 표시:

`git count-objects`

- 모든 객체의 수와 총 디스크 사용량을 계산하여 사람이 읽기 쉬운 단위로 표시:

`git count-objects --human-readable`

- 더 자세한 정보 표시:

`git count-objects --verbose`

- 더 자세한 정보를 사람이 읽기 쉬운 단위로 표시:

`git count-objects --human-readable --verbose`
