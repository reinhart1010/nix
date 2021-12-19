---
layout: page
title: common/gixy (English)
description: "Analyze nginx configuration files."
content_hash: 08690a9900ef8d5280c418424e2e243afedfa0a9
---
# gixy

Analyze nginx configuration files.
More information: <https://github.com/yandex/gixy>.

- Analyze nginx configuration (default path: `/etc/nginx/nginx.conf`):

`gixy`

- Analyze nginx configuration but skip specific tests:

`gixy --skips `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http_splitting</span>

- Analyze nginx configuration with the specific severity level:

`gixy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|-ll|-lll</span>

- Analyze nginx configuration files on the specific path:

`gixy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/configuration_file_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/configuration_file_2</span>
