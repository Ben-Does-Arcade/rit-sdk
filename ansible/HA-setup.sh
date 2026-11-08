docker run -d \
--name homeassistant \
--privileged \
--restart=unless-stopped \
-e TZ=America/New_York \
-v ~/homeassistant:/config \
-v /run/dbus:/run/dbus:ro \
-v /etc/localtime:/etc/localtime:ro \
--network=host \
ghcr.io/home-assistant/home-assistant:dev
