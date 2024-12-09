#!/bin/bash
# .ftl/deploy.sh

set -e

# Load environment-specific configuration
load_env_config() {
    local env=$1
    case $env in
      development)
        export AWS_REGION="us-west-2"
        export DEPLOY_STRATEGY="blue_green"
        ;;
      staging)
        export AWS_REGION="us-east-1"
        export DEPLOY_STRATEGY="canary"
        ;;
      production)
        export AWS_REGION="us-east-1"
        export DEPLOY_STRATEGY="rolling_update"
        ;;
      *)
        echo "Invalid environment: $env"
        exit 1
        ;;
    esac
}

# Build Docker image
build_image() {
    local env=$1
    docker build \
      --build-arg ENVIRONMENT=$env \
      -t message_board_server:$env \
      .
}

# Push to ECR
push_to_ecr(){
    local env=$1
    aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_REGISTRY
    docker tag message_board_server:$env $ECR_REGISTRY/message_board_server:$env
    docker push $ECR_REGISTRY/message_board_server:$env
}

# Deploy to ECS
deploy_to_ecs() {
    local env=$1
    aws ecs update-service \
      --cluster message_board_server-cluster \
      --service message_board_server-service-$env \
      --task-definition message_board_server-task-$env \
      --force-new-deployment
}

# Main deployment function
main() {
    local env=$1

    # Validate input
    if [[ -z "$env" ]]; then
      echo "Usage: $0 <environment>"
      exit 1
    }

    # Load environment-specific configuration
    load_env_config $env

    # Validate AWS credentials and configuration
    aws sts get-caller-identity

    # Build and deploy
    build_image $env
    push-to_ecr $env
    deploy_to_ecr $env

    echo "Deployment to $env completed successfully!"
}

# Run the main function with the provided environment
main "$@"

