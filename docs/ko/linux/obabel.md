---
layout: page
title: linux/obabel (한국어)
description: "화학 관련 데이터를 변환합니다."
content_hash: 88f193053c2e603bc123af3c1b7c25e6f3e8f125
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/obabel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# obabel

화학 관련 데이터를 변환합니다.
더 많은 정보: <https://open-babel.readthedocs.io/en/latest/Command-line_tools/babel.html>.

- .mol 파일을 XYZ 좌표로 변환:

`obabel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mol</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.xyz</span>

- SMILES 문자열을 500x500 그림으로 변환:

`obabel -:"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SMILES</span>`" -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.png</span>` -xp 500`

- SMILES 문자열 파일을 개별 3D .mol 파일로 변환:

`obabel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.smi</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.mol</span>` --gen3D -m`

- 여러 입력을 하나의 그림으로 렌더링:

`obabel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.png</span>
