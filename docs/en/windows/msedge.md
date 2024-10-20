---
layout: page
title: windows/msedge (English)
description: "Modern web browser developed by Microsoft based on the Chromium web browser developed by Google."
content_hash: 18b804fbbadce69e733bd6ba6a85bd23641dfd1a
last_modified_at: 2024-10-20
related_topics:
  - title: Indonesia version
    url: /id/windows/msedge.html
    icon: bi bi-globe
tldri18n_status: 2
---
# msedge

Modern web browser developed by Microsoft based on the Chromium web browser developed by Google.
This command is available instead as `microsoft-edge` for other platforms.
Note: Additional command arguments from `chromium` may also be usable to control Microsoft Edge.
More information: <https://microsoft.com/edge>.

- Open a specific URL or file:

`msedge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com|path/to/file.html</span>

- Open in InPrivate mode:

`msedge --inprivate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Open in a new window:

`msedge --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Open in application mode (without toolbars, URL bar, buttons, etc.):

`msedge --app=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Use a proxy server:

`msedge --proxy-server="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">socks5://hostname:66</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Open with a custom profile directory:

`msedge --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Open without CORS validation (useful to test an API):

`msedge --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --disable-web-security`

- Open with a DevTools window for each tab opened:

`msedge --auto-open-devtools-for-tabs`
