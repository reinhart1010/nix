---
layout: page
title: common/jupyter (中文)
description: "用于创建和共享包含代码、可视化和笔记的文档的 Web 应用程序。"
content_hash: 812d9b8746b767e129a96b117e40429b645256ae
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/jupyter.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jupyter.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/jupyter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jupyter

用于创建和共享包含代码、可视化和笔记的文档的 Web 应用程序。
主要用于数据分析、科学计算和机器学习。
更多信息：<https://jupyter.org>.

- 在当前目录下启动一个 Jupyter notebook 服务器：

`jupyter notebook`

- 打开一个特定的 Jupyter notebook：

`jupyter notebook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">示例.ipynb</span>

- 将特定 Jupyter notebook 导出为其他格式：

`jupyter nbconvert --to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html|markdown|pdf|script</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">示例.ipynb</span>

- 在指定端口启动服务器：

`jupyter notebook --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">端口</span>

- 列出当前正在运行的 notebook 服务器：

`jupyter notebook list`

- 停止当前正在运行的服务器：

`jupyter notebook stop`

- 启动 JupyterLab（如果已安装）于当前目录：

`jupyter lab`
