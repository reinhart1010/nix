---
layout: page
title: common/patch (한국어)
description: "diff 파일을 사용하여 파일(들)을 패치."
content_hash: 8a9fcd152920da8d75a255bb25c3ac7dce7a59f4
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/patch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# patch

diff 파일을 사용하여 파일(들)을 패치.
diff 파일은 `diff` 명령으로 생성되어야 함.
더 많은 정보: <https://manned.org/patch>.

- diff 파일을 사용하여 패치 적용 (파일 이름이 diff 파일에 포함되어야 함):

`patch < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패치.diff</span>

- 특정 파일에 패치 적용:

`patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패치.diff</span>

- 다른 파일에 결과를 작성하여 파일 패치:

`patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패치.diff</span>

- 현재 디렉토리에 패치 적용:

`patch -p1 < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패치.diff</span>

- 패치의 반대로 적용:

`patch -R < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패치.diff</span>
