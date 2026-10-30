# Source lessons

These are condensed lessons from the supplied Apple video library. Titles and API references retain their source-era meaning. Check current official documentation before implementation. Workflow and verification steps in SKILL.md are an editorial synthesis; they are not verbatim Apple requirements.

## 7. WWDC25: Meet Containerization | Apple

Containerization is a Swift framework for managing Linux containers on macOS. Its architecture gives each container a lightweight virtual machine to provide isolation while keeping startup and resource use efficient.

[Original session](https://www.youtube.com/watch?v=JvQtvbhtXmo) · Original library transcript: `transcripts/07-JvQtvbhtXmo.md`

- Package applications and their dependencies together so development, testing, and deployment environments can be reproduced independently of the host. [Evidence at 00:01:28.819](https://www.youtube.com/watch?v=JvQtvbhtXmo&t=88s)

- Distinguish an image from a running container: the image supplies filesystem contents and default configuration used to create an instance. [Evidence at 00:04:26.005](https://www.youtube.com/watch?v=JvQtvbhtXmo&t=266s)

- Per-container virtual machines establish separate security boundaries. Share directories only with the containers that actually need access. [Evidence at 00:06:09.942](https://www.youtube.com/watch?v=JvQtvbhtXmo&t=369s)

- Dedicated container IP addresses simplify direct access to services. CPU and memory resources are allocated for active containers. [Evidence at 00:06:21.987](https://www.youtube.com/watch?v=JvQtvbhtXmo&t=381s)

- The framework exposes image contents through Linux-compatible block devices and supplies Swift utilities for building EXT4 filesystems. [Evidence at 00:05:37.376](https://www.youtube.com/watch?v=JvQtvbhtXmo&t=337s)

- A minimal init system reduces the virtual machine's attack surface. The Swift Static Linux SDK enables its static Linux binary to be cross-compiled from a Mac. [Evidence at 00:08:39.358](https://www.youtube.com/watch?v=JvQtvbhtXmo&t=519s)

- Use the container CLI to explore image pulling and container execution, or use the framework APIs when building your own container-management solution. [Evidence at 00:09:26.138](https://www.youtube.com/watch?v=JvQtvbhtXmo&t=566s)

Visual examples: [Image versus container](https://www.youtube.com/watch?v=JvQtvbhtXmo&t=269s) — The image consists of filesystem contents and configuration, before it becomes a running instance.; [Virtual-machine isolation](https://www.youtube.com/watch?v=JvQtvbhtXmo&t=372s) — Each blue container is enclosed by its own virtual machine above the common macOS host.; [Image filesystem and block devices](https://www.youtube.com/watch?v=JvQtvbhtXmo&t=340s) — The image filesystem is represented as an EXT4 filesystem for the created container.
