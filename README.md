# [Photo Editor: A Modern Breakout Game using Pygame](https://github.com/PythonDecorator)

<br />

![version](https://img.shields.io/badge/version-1.0.0-blue.svg)

--- 

## Table of Contents

* [Overview](#overview)
* [Demo](#demo)
* [Documentation](#documentation)
* [Features](#features)
* [Converting to Executable](#converting-to-executable)
* [Controls](#Controls)
* [Licensing](#license)
* [Reporting Issues](#reporting-issues)
* [Technical Support or Questions](#technical-support-or-questions)
* [Social Media](#Social-media)

<br />

## Overview

Photo Editor is an advanced photo editing desktop application built with Python.

The purpose of this project is to provide users with a versatile and user-friendly photo editing experience right on
their desktops. By combining the power of Python with powerful image manipulation libraries. "Photo Editor" enables
users to enhance, retouch, and transform their photos with a wide range of tools and features.

Whether you're a photography enthusiast or a casual user, this app offers a comprehensive set of tools for achieving
professional-looking edits.

<br />

## Demo

![demo-blog.gif](apps/static/assets/demo/demo-blog.gif)

- **Download the One file .exe file from the dist folder**
- **You don't need to install anything, just download, click and start playing.**

<br />

## Features

> Game main Features

1. ✅ `User-Friendly Interface`: Design an intuitive and visually appealing user interface that
   allows users to easily navigate and utilize the app's functionalities.

2. ✅ `Image Editing Tools:`: Diverse set of image editing tools, including cropping,
   resizing, rotation, and flipping, to provide users with basic editing capabilities.

3. ✅ `Filters and Effects`: Collection of filters and effects to enhance images creatively. Allow users to
   adjust parameters like brightness, contrast, saturation, and more.

4. ✅ `Undo/Redo`: Implement undo and redo functionality, along with a history panel that
   allows users to track their editing steps and revert changes if needed.

5. ✅ `Export`: Enable users to save their edited images in various formats.

<br />

## Documentation

This game was built based on the Customtkinter and Pillow documentation

<br />

## Converting to Executable

PyInstaller is a popular tool that allows you to convert Python scripts into standalone executable files for various
platforms, effectively creating desktop applications.

- You can use PyInstaller options to customize the behavior and appearance of the generated executable. Refer to the
  PyInstaller documentation for more information on available options.
- Keep in mind that PyInstaller generates a self-contained executable, but the size of the executable might be larger
  due
  to the inclusion of the Python interpreter and any dependencies, it's best to use venv to make sure only packages used
  in the
  project are included.
- Be sure to test the generated executable on the
  target platform to ensure everything works as expected.

<br />

> Install modules via `VENV`

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Create the .exe file

```bash
$ pyinstaller main.spec 
```

<br />

## Controls

Press the left or right key to control the paddle.

## License

This project is licensed under the MIT license. See also the attached LICENSE file.

## Reporting Issues

GitHub Issues is the official bug tracker for the Photo Editor.

## Technical Support or Questions

If you have questions contact me okpeamos.ao@gmail.com instead of opening an issue.

- Make sure that you are using the latest version of the Photo Editor. 
- Check the CHANGELOG
- Provide reproducible steps for the issue will shorten the time it takes for it to be fixed.

## Social Media

- Twitter: <https://twitter.com/AmosBrymo67154>
- Instagram: <https://www.instagram.com/pythondecorator>

<br />

---

