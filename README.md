# Sepal

## What Is Sepal?

Sepal is a shell language designed to interop with Trillia.
Sepal itself is extremely small, not even capable of mathematics or control structures.
For anything more complex than file commands, Sepal drops to Trillia and is built to do so readily.

> [!TIP]
> You can enter the Trillia manual [here](https://github.com/TiCaLiBrO/Trillia/blob/main/root/sepalinfo.md). Go wherever your heart takes you.
> This is the [Sepal](https://github.com/TiCaLiBrO/Trillia/blob/main/root/learning/tutorials/sepal/sepalinfo.md) tutorial found within.

## What Does Sepal Solve?

### Multiple Working Directories
Sepal, unlike other shell languages, is designed for multiple working directories.
You can switch between working directories on the fly instead of opening several terminals.

### Automatic Parallelization
Sepal, like Trillia, is designed to know when processes can be parallelized safely, and will do so for tasks that would otherwise take a long time to solve.
As such, it's usually faster than other shell languages.

### Clean Modern Design
Sepal is not some arcane language.
Other shells like Bash are unintuitive and look like magic to those who don't understand.
Sepal is more straightforward and comes with an entirely interactive manual built for teaching the language and Trillia.
The bar for entry is extremely low, and the mental model is simplified.
Sepal is built with a modern design, rejecting POSIX allows it to be more internally consistent with Trillia.

### Version Control & Hot Edits
With Sepal, you can *edit Trillia code ***while it's running***.*
Sepal is designed specifically to be a runtime debugger, editor, and companion for Trillia code.
With runtime analysis, runtime debugging, runtime tracing, and literal hot-fixes, Sepal becomes an essential tool for maximizing productivity, finding the root causes of bugs live as they appear.
Version control is entirely handleable via Sepal, allowing you to test, branch, and commit changes as desired.
Sepal is a shell that can navigate the filesystem, but when running a program, it often turns into a REPL, allowing errors to be fixed as they appear.
Sepal is both a shell and a REPL by design.

### Decompilation
Sepal is designed to decompile Trillia files, allowing them to be edited and recompiled after compilation.
Since Trillia is designed to be losslessly reverse-compilable, Sepal works as the primary way to edit compiled files.


![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://github.com/TiCaLiBrO/Sepal/blob/main/Sepal%20Logo.png)


