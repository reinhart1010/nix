---
layout: page
title: common/crane-export (한국어)
description: "컨테이너 이미지의 파일 시스템을 tarball로 내보냄."
content_hash: cae129c1231ff1f43fbdafed79f91e00111c4638
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/crane-export.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane export

컨테이너 이미지의 파일 시스템을 tarball로 내보냄.
더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

- `stdout`에 tarball을 작성 :

`crane export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>` -`

- 파일에 tarball 쓰기:

`crane export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/tarball</span>

- stdin에서 이미지 읽기:

`crane export - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일이름</span>
