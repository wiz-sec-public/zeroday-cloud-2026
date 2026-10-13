# Kubelet

## Objective and eligibility

Achieve unauthenticated remote code execution in Kubelet through HTTPS `10250` or read-only HTTP `10255` without a token or client certificate, and execute `/flag.sh kubelet` on the target Kubernetes node.

The Kubelet and its default in-process stack are eligible. The node kernel, Docker/containerd escape paths, and other Kubernetes components are excluded.

## Local environment

For your convenience, we have provided a KinD (Kubernetes in Docker) setup that replicates the official competition environment. An exploit that functions correctly against this local setup is highly likely to succeed during the live demonstration.

### Create a Kind cluster

```bash
kind create cluster --name zdc-kubelet --wait 120s --config - <<'EOF'
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
  - role: worker
    kubeadmConfigPatches:
      - |
        kind: JoinConfiguration
        nodeRegistration:
          kubeletExtraArgs:
            read-only-port: "10255"
EOF
kubectl wait --for=condition=Ready node/zdc-kubelet-worker --timeout=120s
```

### Create a test pod

```bash
kubectl apply -f - <<'EOF'
apiVersion: v1
kind: Pod
metadata:
  name: kubelet-no-token
spec:
  automountServiceAccountToken: false
  containers:
    - name: client
      image: curlimages/curl:latest
      command: ["sleep", "infinity"]
EOF
kubectl wait --for=condition=Ready pod/kubelet-no-token --timeout=120s
```

### Test access to the Kubelet APIs

```bash
node_ip="$(kubectl get node zdc-kubelet-worker -o jsonpath='{.status.addresses[?(@.type=="InternalIP")].address}')"

kubectl exec kubelet-no-token -- curl -fsS "http://${node_ip}:10255/pods"

kubectl exec kubelet-no-token -- curl -sk -o /dev/null -w '%{http_code}\n' \
  "https://${node_ip}:10250/pods"
```

## Submission & Eligibility Guidelines

If your exploit requires a configuration different from the one provided or has other specific prerequisites, you must contact the competition organizers in advance to ensure the exploit's eligibility for scoring.

For all inquiries and clarifications, please contact us at zerodaycloud@wiz.io
