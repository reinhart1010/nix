---
layout: page
title: common/jupytext (中文)
description: "将 Jupyter 笔记本转换为纯文本文件，然后再转换回去。"
content_hash: a3ef28aac5e1249e5f926da73489aef4f03dd5f6
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/jupytext.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jupytext.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jupytext

将 Jupyter 笔记本转换为纯文本文件，然后再转换回去。
更多信息：<https://jupytext.readthedocs.io>.

- 将笔记本转换为成对的 `.ipynb`/`.py` 笔记本：

`jupytext --set-formats ipynb,py `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">notebook.ipynb</span>

- 将笔记本转换为 `.py` 文件：

`jupytext --to py `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">notebook.ipynb</span>

- 将 `.py` 文件转换为没有输出的笔记本：

`jupytext --to notebook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">notebook.py</span>

- 将 `.md` 文件转换为笔记本并运行它：

`jupytext --to notebook --execute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">notebook.md</span>

- 更新笔记本中的输入单元格并保留输出和元数据：

`jupytext --update --to notebook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">notebook.py</span>

- 更新笔记本的所有配对表示：

`jupytext --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">notebook.ipynb</span>
