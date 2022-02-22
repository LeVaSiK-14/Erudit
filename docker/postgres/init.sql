CREATE USER erudit_user WITH PASSWORD 'erudit_password';

CREATE DATABASE erudit_db;
GRANT ALL PRIVILEGES ON DATABASE erudit_db TO erudit_user;

