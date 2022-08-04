---
layout: page
title: linux/rspamc (English)
description: "Command-line client for rspamd servers."
content_hash: 562692ca639e2d09dba680d0d91e94c14c92ad4b
---
# rspamc

Command-line client for rspamd servers.
More information: <https://manned.org/rspamc>.

- Train the bayesian filter to recognise an email as spam:

`rspamc learn_spam `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/email_file</span>

- Train the bayesian filter to recognise an email as ham:

`rspamc learn_ham `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/email_file</span>

- Generate a manual report on an email:

`rspamc symbols `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/email_file</span>

- Show server statistics:

`rspamc stat`
