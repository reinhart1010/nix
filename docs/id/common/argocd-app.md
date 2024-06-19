---
layout: page
title: common/argocd-app (Indonesia)
description: "Program baris perintah untuk mengatur aplikasi bersama Argo CD."
content_hash: 25025d9b74e96181d637115228cd7a65fba42b71
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/common/argocd-app.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/argocd-app.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/argocd-app.html
    icon: bi bi-globe
tldri18n_status: 2
---
# argocd app

Program baris perintah untuk mengatur aplikasi bersama Argo CD.
Informasi lebih lanjut: <https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd_app/>.

- Dapatkan daftar aplikasi yang diatur bersama Argo CD:

`argocd app list --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|yaml|wide</span>

- Lihat informasi mengenai suatu aplikasi:

`argocd app get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_aplikasi</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|yaml|wide</span>

- Sebarkan (deploy) aplikasi secara internal (ke dalam klaster yang sama dengan yang dijalankan Argo CD):

`argocd app create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_aplikasi</span>` --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat_url_repositori_dalam_git</span>` --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/repo</span>` --dest-server https://kubernetes.default.svc --dest-namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ns</span>

- Hapus suatu aplikasi:

`argocd app delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_aplikasi</span>

- Aktifkan fitur sinkronisasi otomatis dalam suatu aplikasi:

`argocd app set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_aplikasi</span>` --sync-policy auto --auto-prune --self-heal`

- Pratinjau hasil proses sinkronisasi aplikasi tanpa berdampak kepada klaster yang berjalan (dry-run):

`argocd app sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_aplikasi</span>` --dry-run --prune`

- Tampilkan riwayat penyebaran (deployment) aplikasi:

`argocd app history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_aplikasi</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wide|id</span>

- Batalkan penyebaran dengan memuat (rollback) versi hasil sebaran sebelumnya (dan menghapus sumber daya baru yang tak diduga), berdasarkan nomor induk (ID) riwayat:

`argocd app rollback `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_aplikasi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_riwayat</span>` --prune`
