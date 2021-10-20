RESOURCE_GROUP="course2resourcegroup"
APP_REGISTRY="project2appregistry"

az acr create --resource-group $RESOURCE_GROUP --name $APP_REGISTRY --sku Basic

APP_REGISTRY_LINK="$APP_REGISTRY.azurecr.io"
echo $APP_REGISTRY_LINK
docker login $APP_REGISTRY_LINK

func init --docker-only --python

DOCKER_IMAGE="project2dockerimage"
docker build . -t $DOCKER_IMAGE

docker run -p 8080:80 -it $DOCKER_IMAGE

docker tag $DOCKER_IMAGE $APP_REGISTRY_LINK/$DOCKER_IMAGE

az acr login --name $APP_REGISTRY

docker push $APP_REGISTRY_LINK/$DOCKER_IMAGE

K8SC="project2kubernetescluster"
az aks create \
 --resource-group $RESOURCE_GROUP \
 --name $K8SC \
 --node-count 1 \
 --generate-ssh-keys
 
 
# ERR_CONNECTION_TIMED_OUT accessing kubernetes deployment for Exercise "Containerizing Your App for AKS Deployment"
# https://knowledge.udacity.com/questions/613679

az aks update -n $K8SC -g $RESOURCE_GROUP --attach-acr $APP_REGISTRY


# Get credentials
az aks get-credentials --name $K8SC --resource-group $RESOURCE_GROUP


# https://docs.microsoft.com/en-us/azure/azure-functions/functions-kubernetes-keda#deploying-a-function-app-to-kubernetes

func kubernetes deploy --name $K8SC --image-name $APP_REGISTRY_LINK/$DOCKER_IMAGE:latest --polling-interval 3 --cooldown-period 5



kubectl config get-contexts
