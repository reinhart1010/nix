---
layout: page
title: common/jupyter (English)
description: "Web application to create and share documents that contain code, visualizations and notes."
content_hash: cc7680b8760bc43b707499d079dd161896ce054d
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/jupyter.html
    icon: bi bi-globe
---
# jupyter

Web application to create and share documents that contain code, visualizations and notes.
Primarily used for data analysis, scientific computing and machine learning.
More information: <https://jupyter.org>.

- Start a Jupyter notebook server in the current directory:

`jupyter notebook`

- Open a specific Jupyter notebook:

`jupyter notebook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.ipynb</span>

- Export a specific Jupyter notebook into another format:

`jupyter nbconvert --to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html|markdown|pdf|script</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.ipynb</span>

- Start a server on a specific port:

`jupyter notebook --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- List currently running notebook servers:

`jupyter notebook list`

- Stop the currently running server:

`jupyter notebook stop`

- Start JupyterLab, if installed, in the current directory:

`jupyter lab`
