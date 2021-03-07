[![Think Procedural Cover](https://raw.githubusercontent.com/thinkprocedural/web/master/assets/cover.svg)](https://discord.gg/b8U5Hdy)

<p align="center">
<!-- discord -->
<a href="https://discord.gg/b8U5Hdy">
<img src="https://img.shields.io/discord/230123485668573184?style=flat&colorA=f5f5f5&colorB=f5f5f5&label=&logo=discord&logoColor=000000" />
</a>

<!-- github actions -->
<a href="https://github.com/thinkprocedural/bot/actions?query=workflow%3Aci">
<img src="https://img.shields.io/github/workflow/status/thinkprocedural/bot/ci?style=flat&colorA=f5f5f5&colorB=f5f5f5&label=GitHub%20Actions&logo=github&logoColor=000000" />
</a>

<!-- docker image size -->
<a href="https://hub.docker.com/r/thinkprocedural/bot">
<img src="https://img.shields.io/docker/image-size/thinkprocedural/bot/latest?style=flat&colorA=f5f5f5&colorB=f5f5f5&label=Image%20size&logo=docker&logoColor=000000" />
</a>

<!-- docker image version -->
<a href="https://hub.docker.com/r/thinkprocedural/bot">
<img src="https://img.shields.io/docker/v/thinkprocedural/bot?style=flat&colorA=f5f5f5&colorB=f5f5f5&label=Image%20version&logo=docker&logoColor=000000" />
</a>
</p>

```bash
docker run -d \
    --name=bot \
    -e TOKEN="DISORD_TOKEN" \
    -e PREFIX="!" \
    -e LOGGING_LEVEL="CRITICAL" \
    --restart unless-stopped \
    thinkprocedural/bot
```
