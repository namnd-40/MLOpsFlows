#!/bin/bash

user=$1
sudo groupadd -r $user
sudo useradd -r -s /sbin/nologin -d /dev/null -g $user $user
