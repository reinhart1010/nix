---
layout: page
title: common/convmv (한국어)
description: "한 인코딩에서 다른 인코딩으로 파일 이름(파일 내용 X)을 변환."
content_hash: 844d0187e88620a5eded8424813e47ea63d2ff8f
related_topics:
  - title: English version
    url: /en/common/convmv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/convmv.html
    icon: bi bi-globe
---
# convmv

한 인코딩에서 다른 인코딩으로 파일 이름(파일 내용 X)을 변환.
더 많은 정보: <https://www.j3e.de/linux/convmv/man/>.

- 파일 이름 인코딩 변환 테스트(파일 이름을 실제로 변경하지 마십시오):

`convmv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인코딩_에서</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인코딩_으로</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>

- 파일 이름 인코딩을 변환하고 파일 이름을 새 인코딩으로 변환:

`convmv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인코딩_에서</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인코딩_으로</span>` --notest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>
