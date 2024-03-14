---
layout: page
title: common/gunicorn (中文)
description: "Python 的 WSGI HTTP 服务器。"
content_hash: 5ff735736712bd60434374d321e226ccc4de1ef8
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/gunicorn.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gunicorn

Python 的 WSGI HTTP 服务器。
更多信息：<https://gunicorn.org/>.

- 运行 Python web 应用程序：

`gunicorn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">导入路径：应用程序</span>

- 在 localhost 上监听 8080 端口：

`gunicorn --bind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localhost</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">导入路径：应用程序</span>

- 启用实时自动加载：

`gunicorn --reload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">导入路径：应用程序</span>

- 使用 4 个工作进程处理请求：

`gunicorn --workers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">导入路径：应用程序</span>

- 使用 4 个工作线程处理请求：

`gunicorn --threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">导入路径：应用程序</span>

- 通过 HTTPS 运行应用程序：

`gunicorn --certfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cert.pem</span>` --keyfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key.pem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">导入路径：应用程序</span>
