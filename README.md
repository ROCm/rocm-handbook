# ROCm handbook

The ROCm handbooks target developers who require a unified, book-style
reference for ROCm and HIP. They aggregate documentation from the ROCm portal
and organize it into a structured format optimized for in-depth study and
offline access, available in both PDF and HTML.

This repository is the landing index for the handbook volumes. It does not host
content directly. Instead, it links to the individual volumes, each maintained
in its own repository and published as a separate documentation project.

## Volumes

- **AMD ROCm Programming Guide** — published.
  Repository: [ROCm/AMD-rocm-programming-guide](https://github.com/ROCm/AMD-rocm-programming-guide).
  Published at: <https://rocm-handbook.amd.com/projects/amd-rocm-programming-guide/en/latest/>.

## Build the documentation

This repository builds with Sphinx using the same setup as the other ROCm
documentation projects.

### Linux and WSL

```sh
python3 -mvenv .venv
.venv/bin/python -m pip install -r docs/sphinx/requirements.txt
.venv/bin/python -m sphinx -T -E -b html -d _build/doctrees -D language=en docs _build/html
```

### Windows

```powershell
python -mvenv .venv
.venv\Scripts\python.exe -m pip install -r docs/sphinx/requirements.txt
.venv\Scripts\python.exe -m sphinx -T -E -b html -d _build/doctrees -D language=en docs _build/html
```

Open `_build/html/index.html` in a web browser to view the result.

For further information, see [building documentation](https://rocm.docs.amd.com/en/latest/contribute/building.html).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines and the
[ROCm contribution guide](https://rocm.docs.amd.com/en/latest/contribute/contributing.html)
for the broader process.

## License

See [LICENSE.md](LICENSE.md).
