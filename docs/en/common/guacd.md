---
layout: page
title: common/guacd (English)
description: "Apache Guacamole proxy daemon."
content_hash: 034e7e2f25676fd23760ab690fb8b2569e3337b5
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# guacd

Apache Guacamole proxy daemon.
Support loader for client plugins to interface between the Guacamole protocol and any arbitrary remote desktop protocol (e.g. RDP, VNC, Other).
More information: <https://guacamole.apache.org/>.

- Bind to a specific port on localhost:

`guacd -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4823</span>

- Start in debug mode, keeping the process in the foreground:

`guacd -f -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">debug</span>

- Start with TLS support:

`guacd -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my-cert.crt</span>` -K `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my-key.pem</span>

- Write the PID to a file:

`guacd -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pid</span>
