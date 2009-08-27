Uploading patches on a webpage is hard.  Command line uploading is the future!

### Installation

The script requires Python 2.6.  If this is a terrible burden for you, let me
know.

    STATIC_DEPS=true pip install -e git://github.com/jbalogh/bzattach.git#egg=bzattach

If you want to make the script suck less, check out the source and run

    STATIC_DEPS=true pip install reqs.txt

If you're not installing this in a [virtualenv][1] you're crazy.


The `STATIC_DEPS=true` part may not be necessary on non-Mac systems.

[1]: http://pypi.python.org/pypi/virtualenv
