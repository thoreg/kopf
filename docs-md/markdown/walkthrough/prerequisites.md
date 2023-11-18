# Environment Setup

We need a running Kubernetes cluster and some tools for our experiments.
If you have a cluster already preconfigured, you can skip this section.
Otherwise, let’s install minikube locally (e.g. for MacOS):

* Python >= 3.8 (running in a venv is recommended, though is not necessary).
* [Install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
* [Install minikube](../minikube.md) (a local Kubernetes cluster)
* [Install Kopf](../install.md)

#### WARNING
Unfortunately, Minikube cannot handle the PVC/PV resizing,
as it uses the HostPath provider internally.
You can either skip the [Updating the objects](updates.md) step of this tutorial
(where the sizes of the volumes are changed),
or you can use an external Kubernetes cluster
with real dynamically sized volumes.
