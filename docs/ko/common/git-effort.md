---
layout: page
title: common/git-effort (한국어)
description: "파일의 활동량을 표시하며, 파일별 커밋 수와 \"활성 일수\" 즉, 파일에 기여한 총 일수를 보여줍니다."
content_hash: 71b51ba96d060e328eda0b4ca76b749cb57f61c1
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-effort.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git effort

파일의 활동량을 표시하며, 파일별 커밋 수와 "활성 일수" 즉, 파일에 기여한 총 일수를 보여줍니다.
`git-extras`의 일부입니다.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-effort>.

- 저장소의 각 파일에 대해 커밋 수와 활성 일수를 표시:

`git effort`

- 특정 커밋 수 이상으로 수정된 파일을 표시하며, 커밋 수와 활성 일수를 보여줍니다:

`git effort --above `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- 특정 작성자가 수정한 파일을 표시하며, 커밋 수와 활성 일수를 보여줍니다:

`git effort -- --author="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>`"`

- 특정 시간/날짜 이후에 수정된 파일을 표시하며, 커밋 수와 활성 일수를 보여줍니다:

`git effort -- --since="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">지난달</span>`"`

- 지정된 파일이나 디렉터리만 표시하며, 커밋 수와 활성 일수를 보여줍니다:

`git effort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 특정 디렉터리 내 모든 파일을 표시하며, 커밋 수와 활성 일수를 보여줍니다:

`git effort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더/*</span>
