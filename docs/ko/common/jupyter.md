---
layout: page
title: common/jupyter (한국어)
description: "코드, 시각화 및 노트를 포함한 문서를 생성하고 공유할 수 있는 웹 애플리케이션."
content_hash: 2e23e8cfd2cd0b54b123bd5b0ad55984e0fc8775
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/jupyter.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/jupyter.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/jupyter.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># jupyter

코드, 시각화 및 노트를 포함한 문서를 생성하고 공유할 수 있는 웹 애플리케이션.
주로 데이터 분석, 과학 컴퓨팅 및 머신 러닝에 사용됩니다.
더 많은 정보: <https://jupyter.org>.

- 현재 디렉토리에서 Jupyter 노트북 서버 시작:

`jupyter notebook`

- 특정 Jupyter 노트북 열기:

`jupyter notebook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">예제.ipynb</span>

- 특정 Jupyter 노트북을 다른 형식으로 내보내기:

`jupyter nbconvert --to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html|markdown|pdf|script</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">예제.ipynb</span>

- 특정 포트에서 서버 시작:

`jupyter notebook --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 현재 실행 중인 노트북 서버 나열:

`jupyter notebook list`

- 현재 실행 중인 서버 중지:

`jupyter notebook stop`

- 설치되어 있다면 현재 디렉토리에서 JupyterLab 시작:

`jupyter lab`
