## Faster Than Light (FTL) Deployment

### Prerequisites

- AWS CLI configured
- Docker
- GitHub Actions runner
- AWS ECR repository
- ECS Cluster and Service

### FTL Deployment Workflow

FTL provides a streamlined deployment process across different environments:

#### Manual Deployment

```bash
# Make executable
chmod +x .ftl/deploy.sh

# Deploy to specific environment
.ftl/deploy.sh development
.ftl/deploy.sh staging
.ftl/deploy.sh production
```

#### Automatic Deployment

Pushes to specific branches trigger automatic deployments:
- `develop` branch → Development environment
- `staging` branch → Staging environment
- `main` branch → Production environment

### Environment Configuration

Modify `.ftl/config.yaml` to customize:
- Cloud provider settings
- Deployment strategies
- Scaling configurations
- Monitoring options

### Secrets Management

Configure the following GitHub Secrets:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `ECR_REGISTRY`

### Deployment Strategies

1. **Blue/Green**: Used in development
   - Zero-downtime deployments
   - Easy rollback

2. **Canary**: Used in staging
   - Gradual traffic shifting
   - Risk mitigation

3. **Rolling Update**: Used in production
   - Incremental instance updates
   - Minimal service interruption

### Monitoring

- CloudWatch logs and metrics
- 30-day log retention
- CPU utilization tracking

## Troubleshooting

- Verify AWS CLI configuration
- Check GitHub Actions logs
- Ensure proper IAM roles and permissions
- Validate `.ftl/config.yaml` settings
```

To implement this:

1. Install FTL CLI (refer to FTL GitHub repository)
2. Set up AWS infrastructure
3. Configure GitHub Secrets
4. Push to respective branches for deployment
