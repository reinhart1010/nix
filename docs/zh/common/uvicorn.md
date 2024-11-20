---
layout: page
title: common/uvicorn (中文)
description: "Python 的 ASGI HTTP 服务器，适用于异步项目。"
content_hash: 62fed37ffb69a086b50d23ee4957c0c2e4b24af6
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/common/uvicorn.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/uvicorn.html
    icon: bi bi-globe
tldri18n_status: 2
---
# uvicorn

Python 的 ASGI HTTP 服务器，适用于异步项目。
更多信息：<https://www.uvicorn.org/>.

- 运行 Python Web 应用：

`uvicorn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">导入路径:应用对象</span>

- 在本地主机上监听端口 8080：

`uvicorn --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localhost</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">导入路径:应用对象</span>

- 启用实时重新加载：

`uvicorn --reload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">导入路径:应用对象</span>

- 使用 4 个工作进程处理请求：

`uvicorn --workers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">导入路径:应用对象</span>

- 通过 HTTPS 运行应用：

`uvicorn --ssl-certfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cert.pem</span>` --ssl-keyfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key.pem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">导入路径:应用对象</span>
