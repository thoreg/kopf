# Minikube

To develop the framework and the operators in an isolated Kubernetes cluster,
use [minikube](https://github.com/kubernetes/minikube).

MacOS:

```bash
brew install docker-machine-driver-hyperkit
sudo chown root:wheel /usr/local/opt/docker-machine-driver-hyperkit/bin/docker-machine-driver-hyperkit
sudo chmod u+s /usr/local/opt/docker-machine-driver-hyperkit/bin/docker-machine-driver-hyperkit

brew cask install minikube
minikube config set vm-driver hyperkit
```

Start the minikube cluster:

```bash
minikube start
minikube dashboard
```

It automatically creates and activates the kubectl context named `minikube`.
If not, or if you have multiple clusters, activate it explicitly:

```bash
kubectl config get-contexts
kubectl config current-context
kubectl config use-context minikube
```

For the minikube cleanup (to release the CPU/RAM/disk resources):

```bash
minikube stop
minikube delete
```

#### SEE ALSO
For even more information, read the [Minikube installation manual](https://kubernetes.io/docs/tasks/tools/install-minikube/).
