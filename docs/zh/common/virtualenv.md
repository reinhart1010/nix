---
layout: page
title: common/virtualenv (中文)
description: "创建被隔离的的 Python 虚拟环境。"
content_hash: 48f389751fa9ef6478d18ba6c4d8ec20992c882b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/virtualenv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virtualenv

创建被隔离的的 Python 虚拟环境。
更多信息：<https://virtualenv.pypa.io/>.

- 创建新环境：

`virtualenv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/venv</span>

- 自定义提示符：

`virtualenv --prompt=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt_prefix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/venv</span>

- 为虚拟环境使用不同的 Python 版本：

`virtualenv --python=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pythonbin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/venv</span>

- 启动（选择）环境：

`source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/venv</span>`/bin/activate`

- 停止环境：

`deactivate`
