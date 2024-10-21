---
layout: page
title: common/fossil-commit (한국어)
description: "파일을 Fossil 저장소에 커밋."
content_hash: b76bb3dacfd87659382a662a60b364b13b91dba3
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/fossil-commit.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/fossil-commit.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fossil-commit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fossil commit

파일을 Fossil 저장소에 커밋.
더 많은 정보: <https://fossil-scm.org/home/help/commit>.

- 현재 체크아웃의 모든 변경 사항을 포함하는 새로운 버전을 만듬; 사용자에게 설명을 요청하는 메시지가 표시됨:

`fossil commit`

- 지정된 설명을 사용하여, 현재 체크아웃의 모든 변경 사항을 포함하는 새 버전을 만듬:

`fossil commit --comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코멘트</span>`"`

- 특정 파일에서 읽은 설명과 함께 현재 체크아웃의 모든 변경 사항을 포함하는 새 버전을 생성:

`fossil commit --message-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/커밋_메시지</span>

- Create a new version containing changes from the specified files; user will be prompted for a comment:

`fossil commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>
