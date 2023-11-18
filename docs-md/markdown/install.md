# Installation

Prerequisites:

* Python >= 3.8 (CPython and PyPy are officially tested and supported).

To install Kopf:

```bash
pip install kopf
```

If you use some of the managed Kubernetes services which require a sophisticated
authentication beyond username+password, fixed tokens, or client SSL certs
(also see [authentication piggy-backing](authentication.md#auth-piggybacking)):

```bash
pip install kopf[full-auth]
```

If you want extra i/o performance under the hood, install it as (also see [Custom event loops](embedding.md#custom-event-loops)):

```bash
pip install kopf[uvloop]
```

Unless you use the standalone mode,
create a few Kopf-specific custom resources in the cluster:

```bash
kubectl apply -f https://github.com/nolar/kopf/raw/main/peering.yaml
```

Optionally, if you are going to use the examples or the code snippets:

```bash
kubectl apply -f https://github.com/nolar/kopf/raw/main/examples/crd.yaml
```

You are ready to go:

```bash
kopf --help
kopf run --help
kopf run examples/01-minimal/example.py
```
