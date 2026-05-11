# Amphibious Bot — Contributing Guide

Thank you for your interest in contributing!

## Branches
| Branch | Purpose |
|--------|---------|
| `main` | Stable, report-consistent code |
| `dev`  | Active development |
| `feature/<name>` | New features |

## Workflow
1. Fork → `git checkout -b feature/your-feature`
2. Make changes, add tests/comments
3. `git commit -m "feat: short description"`
4. Open a Pull Request against `dev`

## Code Style
- **Arduino / C++**: follow Arduino style guide, comment all pin definitions
- **Python / ROS2**: PEP8, docstrings on all launch functions
- **XACRO/URDF**: indent 2 spaces, comment every link and joint

## Issues
Please use GitHub Issues for bugs and feature requests.
