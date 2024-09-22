---
layout: page
title: common/aws-history (한국어)
description: "AWS CLI 명령어 대한 명령어 입력 기록을 인쇄 (AWS CLI 명령어 입력 기록 권한이 활성화되어야 함)."
content_hash: 47c004474c6feb76566e56b94bad34d84260c079
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/aws-history.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-history.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-history.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws history

AWS CLI 명령어 대한 명령어 입력 기록을 인쇄 (AWS CLI 명령어 입력 기록 권한이 활성화되어야 함).
더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/history/>.

- 명령어 ID로 명령 기록 나열:

`aws history list`

- 명령어 ID가 지정된 특정 명령과 관련된 이벤트 표시:

`aws history show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_아이디</span>
