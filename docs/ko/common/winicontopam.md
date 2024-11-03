---
layout: page
title: common/winicontopam (한국어)
description: "Windows ICO 파일을 PAM 파일로 변환."
content_hash: c56c11c68be5493a4bc31eb1ba195ddc37e1d7e4
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/winicontopam.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/winicontopam.html
    icon: bi bi-globe
tldri18n_status: 2
---
# winicontopam

Windows ICO 파일을 PAM 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/winicontopam.html>.

- ICO 파일을 읽고 그 안에 포함된 최고 품질의 이미지를 PAM 형식으로 변환:

`winicontopam `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.ico</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>

- 입력 파일의 모든 이미지를 PAM으로 변환:

`winicontopam -allimages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.ico</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>

- 입력 파일의 n번째 이미지를 PAM으로 변환:

`winicontopam -image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.ico</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>

- 추출할 이미지가 그라데이션 투명 데이터와 AND 마스크를 포함하는 경우, 출력 PAM 파일의 다섯 번째 채널에 AND 마스크를 작성:

`winicontopam -andmasks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.ico</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>
