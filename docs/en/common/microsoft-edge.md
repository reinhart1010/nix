---
layout: page
title: common/microsoft-edge (English)
description: "Modern web browser developed by Microsoft based on the Chromium web browser developed by Google."
content_hash: 98dab209436aa9cd9df648a491e627653aaa3307
last_modified_at: 2024-10-20
related_topics:
  - title: Indonesia version
    url: /id/common/microsoft-edge.html
    icon: bi bi-globe
tldri18n_status: 2
---
# microsoft-edge

Modern web browser developed by Microsoft based on the Chromium web browser developed by Google.
This command is available instead as `msedge` for Windows.
Note: Additional command arguments from `chromium` may also be usable to control Microsoft Edge.
More information: <https://microsoft.com/edge>.

- Open a specific URL or file:

`microsoft-edge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com|path/to/file.html</span>

- Open in InPrivate mode:

`microsoft-edge --inprivate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Open in a new window:

`microsoft-edge --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Open in application mode (without toolbars, URL bar, buttons, etc.):

`microsoft-edge --app=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Use a proxy server:

`microsoft-edge --proxy-server="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">socks5://hostname:66</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Open with a custom profile directory:

`microsoft-edge --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Open without CORS validation (useful to test an API):

`microsoft-edge --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --disable-web-security`

- Open with a DevTools window for each tab opened:

`microsoft-edge --auto-open-devtools-for-tabs`
