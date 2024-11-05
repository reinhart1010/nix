---
layout: page
title: common/jupytext (한국어)
description: "Jupyter 노트북을 일반 텍스트 문서로 변환하고, 다시 노트북으로 변환합니다."
content_hash: fda124e347bfac1dfbaa684d124d41f9864207ac
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/jupytext.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/jupytext.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># jupytext

Jupyter 노트북을 일반 텍스트 문서로 변환하고, 다시 노트북으로 변환합니다.
더 많은 정보: <https://jupytext.readthedocs.io>.

- 노트북을 `.ipynb`/`.py`로 쌍으로 변환:

`jupytext --set-formats ipynb,py `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노트북.ipynb</span>

- 노트북을 `.py` 파일로 변환:

`jupytext --to py `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노트북.ipynb</span>

- `.py` 파일을 출력 없이 노트북으로 변환:

`jupytext --to notebook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노트북.py</span>

- `.md` 파일을 노트북으로 변환하고 실행:

`jupytext --to notebook --execute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노트북.md</span>

- 노트북의 입력 셀을 업데이트하고 출력 및 메타데이터를 유지:

`jupytext --update --to notebook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노트북.py</span>

- 노트북의 모든 쌍으로 연결된 표현 업데이트:

`jupytext --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노트북.ipynb</span>
