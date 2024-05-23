---
layout: page
title: common/spfquery (English)
description: "Query Sender Policy Framework records to validate e-mail senders."
content_hash: 56f76c53c50428335afa072048130c96a6f86f4c
last_modified_at: 2024-05-23
tldri18n_status: 2
---
# spfquery

Query Sender Policy Framework records to validate e-mail senders.
More information: <https://manned.org/spfquery>.

- Check if an IP address is allowed to send an e-mail from the specified e-mail address:

`spfquery -ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>` -sender `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sender@example.com</span>

- Turn on debugging output:

`spfquery -ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>` -sender `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sender@example.com</span>` --debug`
