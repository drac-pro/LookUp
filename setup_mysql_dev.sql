-- script that prepares a MySQL server for the project.
-- This script also creates a new user and grand privileges.
CREATE DATABASE IF NOT EXISTS lookup_dev_db;
CREATE USER IF NOT EXISTS 'lookup_dev'@'localhost' IDENTIFIED BY 'lookup_dev_pwd123';
GRANT ALL PRIVILEGES ON lookup_dev_db.* TO 'lookup_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'lookup_dev'@'localhost';
