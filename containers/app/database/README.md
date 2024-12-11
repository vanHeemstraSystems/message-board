# Message Board Database

PostgreSQL database configuration for the Message Board application.

## Overview

This directory contains the PostgreSQL database setup and configuration files for both development and production environments.

## Directory Structure

```
database/
├── Dockerfile.dev              # Development Docker configuration
├── postgresql.conf.dev         # PostgreSQL development configuration
├── postgresql.conf.prod        # PostgreSQL production configuration
├── README.md                   # This file
└── sample.env                  # Sample environment variables
```

## Configuration Files

- `postgresql.conf.dev`: Development-specific PostgreSQL settings
- `postgresql.conf.prod`: Production-specific PostgreSQL settings

## Environment Variables

Copy `sample.env` to `.env` and adjust the values:

```env
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=message_board
```

## Development Setup

1. Build the development container:
```bash
docker compose build database
```

2. Start the database:
```bash
docker compose up database
```

## Production Deployment

1. Use the production configuration:
```bash
cp postgresql.conf.prod postgresql.conf
```

2. Build and run with production settings:
```bash
docker compose -f docker-compose.prod.yml up database
```

## Database Maintenance

### Backup
```bash
docker exec message-board-db pg_dump -U postgres message_board > backup.sql
```

### Restore
```bash
docker exec -i message-board-db psql -U postgres message_board < backup.sql
```

## Security Notes

- Always use strong passwords in production
- Keep your PostgreSQL version updated
- Regularly backup your database
- Use SSL in production

## Contributing

1. Create a feature branch
2. Make your changes
3. Submit a pull request

## License

MIT License - see the main project LICENSE file for details
