Cisco AnyConnect breaks boot2docker.  See, for example, https://github.com/boot2docker/boot2docker/issues/392.

There are many proposed fixes, but this (almost) worked for me: https://github.com/boot2docker/boot2docker/issues/392#issuecomment-68563869.

Try:
boot2docker init
vboxmanage modifyvm "boot2docker-vm" --natpf1 "docker,tcp,127.0.0.1,2376,,2376"
vboxmanage modifyvm "boot2docker-vm" --natpf1 "dockerweb,tcp,127.0.0.1,8080,,8080"
boot2docker up
$(boot2docker shellinit)
export DOCKER_HOST=tcp://127.0.0.1:2376

VIVO can be reached at http://localhost:8080/vivo
