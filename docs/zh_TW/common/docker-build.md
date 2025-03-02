---
layout: page
title: common/docker-build (中文 (繁體, 台灣))
description: "從 Dockerfile 建立 Docker 映像檔 (Image)。"
content_hash: 44e0a23bcac5f124c3846366761759cc96882338
last_modified_at: 2025-03-02
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
  - title: 中文 version
    url: /zh/common/docker-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker build

從 Dockerfile 建立 Docker 映像檔 (Image)。
更多資訊：<https://docs.docker.com/reference/cli/docker/buildx/build/>.

- 使用當前目錄的 Dockerfile 建立映像檔：

`docker build .`

- 從指定的網址下載 Dockerfile 來建立映像檔：

`docker build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github.com/creack/docker-firefox</span>

- 建立 Docker 映像檔並加上標籤：

`docker build --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名稱:標籤</span>` .`

- 不使用建構上下文（Build Context）來建立映像檔：

`docker build --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名稱:標籤</span>` - < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Dockerfile</span>

- 在建構映像檔時不使用快取：

`docker build --no-cache --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名稱:標籤</span>` .`

- 使用特定的 Dockerfile 來建構映像檔：

`docker build --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Dockerfile</span>` .`

- 在建構時傳遞自訂的變數：

`docker build --build-arg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HTTP_PROXY=http://10.20.30.2:1234</span>` --build-arg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FTP_PROXY=http://40.50.60.5:4567</span>` .`
