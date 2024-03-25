CREATE USER 'admindjango'@'%' IDENTIFIED BY 'employee@123!';
GRANT ALL PRIVILEGES ON *.* TO 'admindjango'@'%';
FLUSH PRIVILEGES;
