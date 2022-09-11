# mobi2cbz

Convert e-book files consisting of fixed layouts to cbz files.

## Usage

```powershell
# Set the path to source file. (mobi/prc/azw/azw3/azw4)
# The output destination of cbz file is source file directory.
mobi2cbz <SRC_PATH>

# Optionally set the path to output destination.
mobi2cbz <SRC_PATH> <DST_PATH>
```

## Install

```text
pip install git+https://github.com/1b0325h/mobi2cbz
```

**Local:**

```text
python setup.py install
```

## License Information

### KindleUnpack (https://github.com/kevinhendricks/KindleUnpack)

```
Based on initial mobipocket version Copyright © 2009 Charles M. Hannum <root@ihack.net>
Extensive Extensions and Improvements Copyright © 2009-2014
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.
```
