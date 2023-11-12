---
layout: page
title: common/uvicorn (English)
description: "Python ASGI HTTP Server, for asynchronous projects."
content_hash: dcf0e54997072c8d0ac8d78a746a78aaba74838f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# uvicorn

Python ASGI HTTP Server, for asynchronous projects.
More information: <https://www.uvicorn.org/>.

- Run Python web app:

`uvicorn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import.path:app_object</span>

- Listen on port 8080 on localhost:

`uvicorn --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localhost</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import.path:app_object</span>

- Turn on live reload:

`uvicorn --reload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import.path:app_object</span>

- Use 4 worker processes for handling requests:

`uvicorn --workers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import.path:app_object</span>

- Run app over HTTPS:

`uvicorn --ssl-certfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cert.pem</span>` --ssl-keyfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key.pem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import.path:app_object</span>
