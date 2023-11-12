---
layout: page
title: common/sqlmap (English)
description: "Detect and exploit SQL injection flaws."
content_hash: 5f85407b3bd244c5bec489b02355da6ad4a881cf
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# sqlmap

Detect and exploit SQL injection flaws.
More information: <https://sqlmap.org>.

- Run sqlmap against a single target URL:

`python sqlmap.py -u "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://www.target.com/vuln.php?id=1</span>`"`

- Send data in a POST request (`--data` implies POST request):

`python sqlmap.py -u "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://www.target.com/vuln.php</span>`" --data="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id=1</span>`"`

- Change the parameter delimiter (& is the default):

`python sqlmap.py -u "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://www.target.com/vuln.php</span>`" --data="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query=foobar;id=1</span>`" --param-del="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">;</span>`"`

- Select a random `User-Agent` from `./txt/user-agents.txt` and use it:

`python sqlmap.py -u "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://www.target.com/vuln.php</span>`" --random-agent`

- Provide user credentials for HTTP protocol authentication:

`python sqlmap.py -u "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://www.target.com/vuln.php</span>`" --auth-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Basic</span>` --auth-cred "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testuser:testpass</span>`"`
