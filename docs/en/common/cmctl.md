---
layout: page
title: common/cmctl (English)
description: "A CLI tool that can help you to manage cert-manager resources inside your cluster."
content_hash: 3be0f6805d1899f3127d01e268a68143c3840a40
---
# cmctl

A CLI tool that can help you to manage cert-manager resources inside your cluster.
Check cert signing status, approve/deny requests, and issue new certificate requests.
More information: <https://cert-manager.io/docs/usage/cmctl/>.

- Check if the cert-manager API is ready:

`cmctl check api`

- Check the status of a certificate:

`cmctl status certificate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cert_name</span>

- Create a new certificate request based on an existing certificate:

`cmctl create certificaterequest my-cr --from-certificate-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cert.yaml</span>

- Create a new certificate request, fetch the signed certificate, and set a maximum wait time:

`cmctl create certificaterequest my-cr --from-certificate-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cert.yaml</span>` --fetch-certificate --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20m</span>
