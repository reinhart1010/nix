---
layout: page
title: common/pbmreduce (한국어)
description: "PBM 이미지를 비례적으로 축소."
content_hash: d881bb8b030afc8a7e666ceb4ad92f2dfee9dc1f
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pbmreduce.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pbmreduce

PBM 이미지를 비례적으로 축소.
같이 보기: `pamenlarge`, `pamditherbw`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmreduce.html>.

- 지정한 이미지를 지정한 비율로 축소:

`pbmreduce `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>

- 단순 임계값을 사용하여 축소:

`pbmreduce -threshold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>

- 모든 양자화에 지정한 임계값 사용:

`pbmreduce -value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.6</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>
