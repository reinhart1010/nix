---
layout: page
title: common/docker-build (中文)
description: "从 Dockerfile 打包镜像。"
content_hash: f9e6dfd3d634f48a6c42230311e078abf3292352
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-build.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-build.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-build.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/docker-build.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-build.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-build.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-build.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-build.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker build

从 Dockerfile 打包镜像。
更多信息：<https://docs.docker.com/engine/reference/commandline/build/>.

- 使用当前目录下的 Dockerfile 打包一个 docker 镜像：

`docker build .`

- 从指定 URL 的 Dockerfile 打包 docker 镜像：

`docker build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github.com/creack/docker-firefox</span>

- 打包一个 docker 镜像并指定镜像的标签：

`docker build --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name:tag</span>` .`

- 打包一个没有上下文的 docker 镜像：

`docker build --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name:tag</span>` - < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Dockerfile</span>

- 打包镜像时不使用缓存：

`docker build --no-cache --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name:tag</span>` .`

- 使用指定的 Dockerfile 打包一个 docker 镜像：

`docker build --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Dockerfile</span>` .`

- 传入自定义变量用于打包：

`docker build --build-arg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HTTP_PROXY=http://10.20.30.2:1234</span>` --build-arg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FTP_PROXY=http://40.50.60.5:4567</span>` .`
