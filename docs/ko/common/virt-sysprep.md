---
layout: page
title: common/virt-sysprep (한국어)
description: "가상 머신 이미지를 재설정, 비구성 또는 사용자 정의."
content_hash: 829ae368f5db2a9c588d6314b33e3b85d962ea77
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/virt-sysprep.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># virt-sysprep

가상 머신 이미지를 재설정, 비구성 또는 사용자 정의.
더 많은 정보: <https://manned.org/virt-sysprep>.

- 지원되는 모든 작업 나열 (활성화된 작업은 별표로 표시됨):

`virt-sysprep --list-operations`

- 활성화된 모든 작업을 실행하되 실제로 변경사항을 적용하지 않음:

`virt-sysprep --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_이름</span>` --dry-run`

- 지정된 작업만 실행:

`virt-sysprep --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_이름</span>` --operations `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업1,작업2,...</span>

- 새로운 `/etc/machine-id` 파일을 생성하고 사용자 정의를 활성화하여 네트워크 충돌을 피하기 위해 호스트 이름을 변경할 수 있도록 설정:

`virt-sysprep --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_이름</span>` --enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_정의</span>` --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_이름</span>` --operation `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">machine-id</span>
