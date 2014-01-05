HACKING
=======

Python
------

First
`````

- Step 1: Read http://www.python.org/dev/peps/pep-0008/
- Step 2: Read http://www.python.org/dev/peps/pep-0008/ again
- Step 3: Read on

General
```````

- Optimize for readability; whitespace is your friend.
- Put two newlines between top-level code (funcs, classes, etc.)
- Put one newline between methods in classes and anywhere else.
- Use blank lines to group related logic.
- Never write ``except:`` (use ``except Exception:`` instead, at
  the very least).
- All classes must inherit from ``object`` (explicitly).
- Use single-quotes for strings unless the string contains a
  single-quote.
- Use the double-quote character for blockquotes (``"""``, not ``'''``)
- USE_ALL_CAPS_FOR_GLOBAL_CONSTANTS

Imports
```````

- Do not import objects, only modules
- Do not import more than one module per line
- Do not make relative imports
- Order your imports by the full module path
- Organize your imports in lexical order (TBD)

Git
---

Branching model
```````````````

There are 2 main branches with infinite lifetime: master and develop.
* We consider origin/master to be the main branch where the source code
of HEAD always reflects a production-ready state.
* We consider origin/develop to be the main branch where the source code
of HEAD always reflects a state with the latest
delivered development changes for the next release.

So, every time you make a patch, it will be integrated in develop branch.
At every release, the master is merged with develop.

Feature branches
````````````````

No one should make commits directly to develop branch. Instead, when you
create a patch, you should create a feature branch.
All feature branches MUST be merged into develop. Also, they should only exist
in developers' forks, not in origin.
They can have any name, except master, develop, release-\*, hotfix-\*.

When starting work on a new feature, branch out of from develop branch:

.. code-block:: bash

    $ git checkout -b myfeature develop
    $ git push origin myfeature

To integrate a feature branch into develop:

.. code-block:: bash

    $ git checkout develop
    Switched to branch 'develop'
    $ git merge --no-ff myfeature
    [...]
    (Summary of changes)
    $ git branch -d myfeature
    Deleted branch myfeature (was 05e9557).
    $ git push origin develop

The --no-ff flag causes the merge to always create a new commit object,
even if the merge could be performed with a fast-forward.
This avoids losing information about the historical existence of a feature
branch and groups together all commits that together added the feature.

Release branches
````````````````

Release branches support preparation for a new production release. Their purpose
is to allow small changes (correcting typos small bug fixes), while develop branch
remins open for new patches. All features tagged for the current version must
be integrated into develop by this time. Patches added to develop branch after this
one was created will be added to the next release. Release branches should be merged
with master and develop.

Their name should be release-\* and should indicate the version number.

.. code-block:: bash

    $ git checkout -b release-x.y develop
    $ git commit -m "Release x.y"
    $ git checkout master
    $ git merge --no-ff release-x.y
    $ git tag -a x.y
    $ git push --tags

Then integrates into the develop branch :

.. code-block:: bash

    $ git checkout develop
    $ git merge --no-ff release-x.y

And suppress the release branch:

.. code-block:: bash

    $ git branch -d release-x.y


Hotfix branches
```````````````

Hotfix branches are used to fix bugs in a production version. When a bug is found in
a production version, a hotfix branch should be branched off from master.
After fixing the bug, it should be merged into master and develop. When a release
branch currently exists, hotfix branches must be merged into that instead of develop.

Their name should be hotfix-\* and should indicate the version number.

The creation and merge of release and hotfix branches is simillar to those from
 feature branches.

.. code-block:: bash

    $ git checkout -b hotfix-x.y.z develop
    $ git commit -m "FIX x.y.z"
    $ git checkout master
    $ git merge --no-ff hotfix-x.y.z
    $ git tag -a x.y.z
    $ git push --tags

Then integrates into the develop branch :

.. code-block:: bash

    $ git checkout develop
    $ git merge --no-ff hotfix-x.y.z

And suppress the hotfix branch:

.. code-block:: bash

    $ git branch -d hotfix-x.y.z
