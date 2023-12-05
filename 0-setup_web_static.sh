#!/usr/bin/env bash
# This script sets up web servers for the deployment of web_static.

if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

nginx_config="/etc/nginx/sites-available/default"
sudo sed -i '/location \/hbnb_static {/s/location \/hbnb_static {/location \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;/' "$nginx_config"

sudo service nginx restart

exit 0
