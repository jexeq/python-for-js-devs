# Package Management in Python

Package management is crucial for managing dependencies and libraries in your Python projects. This guide covers how to install, upgrade, and uninstall packages using `pip`, Python's package manager.

## What is `pip`?

`pip` stands for "Pip Installs Packages" and is the default package manager for Python. It allows you to install packages from the Python Package Index (PyPI) and manage your project dependencies effectively.

## Installing Packages

To install a package using `pip`, use the following command:

```bash
pip install package_name
```

### Example

To install NumPy, run:

```bash
pip install numpy
```

## Upgrading Packages

You can upgrade an already installed package to the latest version by using the --upgrade flag

```bash
pip install --upgrade package_name
```

example

```bash
pip install --upgrade numpy
```

## Uninstalling Packages

To remove a package that you no longer need, you can use the uninstall command:

```bash
pip uninstall package_name
```

example

```bash
pip uninstall numpy
```

## Listing Installed Packages

To see a list of all installed packages in your current environment, use:

```bash
pip list
```

## Saving Packages List

To save your project's dependencies to a requirements.txt file, use:

```bash
pip freeze > requirements.txt
```

This file can later be used to recreate the environment by installing all listed packages with:

```bash
pip install -r requirements.txt
```
