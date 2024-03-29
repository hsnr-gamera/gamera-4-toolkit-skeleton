# Skeleton Toolkit for Gamera 4


Toolkit skeleton for Gamera 4 and Python 3.

## What is a toolkit?


A toolkit is a way to distribute code that uses Gamera but is not
included in the Gamera source tree.  This could be entire
applications that process images and return symbolic
results (eg. an OCR package), or simply a library of utility
functions (eg. for color image processing).

The Gamera toolkit framework actually provides very little beyond the
standard Python package and module system on which it is based:

- A special Python setuptools-based framework for building Gamera
  plugins more conveniently.
- Support for adding a toolkit-specific drop-down menu to the Gamera
  GUI.

If neither of these features is necessary for your project, you may
decide to simply release your application or library as a standard
Python package.

## Creating a toolkit


### The directory hierarchy


Toolkits require a number of different files in a directory
hierarchy.  Here we assume the toolkit is called ``my_toolkit``.

<table class="docutils">
<colgroup>
<col>
<col>
<col>
</colgroup>
<tbody>
<tr><td rowspan="2">./</td>
<td colspan="2">Basic information files for building the toolkit</td>
</tr>
<tr><td>setup.py</td>
<td>A Python setuptools-based build script.</td>
</tr>
<tr><td rowspan="3">gamera/</td>
<td colspan="2">All the files needed by Gamera at runtime.
Since Python is interpreted, these means
Python source files.</td>
</tr>
<tr><td>toolkits/
my_toolkit</td>
<td>This is where the Python source code of the
toolkit goes.</td>
</tr>
<tr><td>toolkits/
my_toolkit/
plugins/</td>
<td>This is where the Gamera plugins for the
toolkit go.</td>
</tr>
<tr><td rowspan="2">include/</td>
<td colspan="2">C++ header (<tt class="docutils literal">.hpp</tt>) files.</td>
</tr>
<tr><td>plugins/</td>
<td>Source code for the C++-based plugins.</td>
</tr>
<tr><td>scripts/</td>
<td colspan="2">Command line scripts</td>
</tr>
<tr><td rowspan="4">doc/</td>
<td colspan="2">Documentation</td>
</tr>
<tr><td>gendoc.py</td>
<td>A script to generate the documentation using
the Gamera documentation system.</td>
</tr>
<tr><td>src/</td>
<td>The source files for the narrative
documentation.</td>
</tr>
<tr><td>html/</td>
<td>The HTML output from the Gamera documentation
system.</td>
</tr>
</tbody>
</table>

Some toolkits may go beyond this, of course, by including ``.cpp``
files in a ``src/`` directory or documentation in a ``doc/``
directory.

**Note:** At present, toolkit documentation does not compile along with the main Gamera documentation.  I have not yet decided whether this should be considered a feature or a bug.

### The skeleton toolkit

For convenience, a minimal skeleton of a toolkit is provided and
available from the files section of the [Gamera github site](https://github.com/hsnr-gamera).

This skeleton provides the very minimum needed to create a toolkit.
You will need to change all the references to the toolkit name
(Skeleton) throughout its source.  The ``rename.py`` script is
provided for this purpose. For example::

  ```python rename.py my_toolkit```

will rename and edit all of the files to create a new toolkit called
``my_toolkit``.

### Editing the files


The files included in the skeleton toolkit are self-documenting.  They
should require only minimal editing.  Mainly, toolkit authors will be
adding their own Python modules and Gamera plugins to the toolkit.

#### setup.py


You only need to edit this file if you are doing anything more complex
than installing Python modules and building Gamera plugins.  For
instance, if you are building and linking to a third-party library.
Since this script is based on Python setuptools, the setuptools
documentation is the best resource for how to do that.

#### MANIFEST.in


If you need to include more data files to your toolkit distrubution,
you will need to edit this file.  The format is described in the
setuptools documentation.

#### gamera/toolkits/my_toolkit/__init__.py


If you want to add a drop-down menu to the Gamera GUI shell, you can
edit this file.  It is self-documenting.  You will probably want to
remove the example menu items that are included in the skeleton.

#### Plugins


Writing plugins is described in detail [here](https://gamera.informatik.hsnr.de/docs/gamera-docs/writing_plugins.html).  The Python metadata
files for a toolkit go in ``gamera/toolkits/my_toolkit/plugins/``, and
the C++ source code goes in ``include/plugins/``.

#### Python modules


The Python modules in your toolkit should go in
``gamera/my_toolkit/skeleton``.

## Building and installing a toolkit


Building and installing toolkits is very similar to building and
installing Gamera itself.  

**You must ensure that Gamera is installed and working before
attempting to build and install a Gamera toolkit.**

The complete instructions for building Gamera toolkits is included in
the skeleton example in the INSTALL file.  You should redistribute
this file with your toolkit.


## Authors and License


(c) 2004 Michael Droettboom  
(c) 2023 Christoph Dalitz and Olaf Braun

This software is distributed under the GNU General Public License.
See the file LICENSE for more information.
