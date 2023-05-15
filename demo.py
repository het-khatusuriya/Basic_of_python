Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=5
a
5
a=10
b=20
c=a+b
c
30
help
Type help() for interactive help, or help(object) for help about object.
help()

Welcome to Python 3.10's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.10/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> modules

Please wait a moment while I gather a list of all available modules...

__future__          argparse            help                sched
__main__            array               help_about          scrolledlist
_abc                ast                 history             search
_aix_support        asynchat            hmac                searchbase
_ast                asyncio             html                searchengine
_asyncio            asyncore            http                secrets
_bisect             atexit              hyperparser         select
_blake2             audioop             idle                selectors
_bootsubprocess     autocomplete        idle_test           setuptools
_bz2                autocomplete_w      idlelib             shelve
_codecs             autoexpand          imaplib             shlex
_codecs_cn          base64              imghdr              shutil
_codecs_hk          bdb                 imp                 sidebar
_codecs_iso2022     binascii            importlib           signal
_codecs_jp          binhex              inspect             site
_codecs_kr          bisect              io                  smtpd
_codecs_tw          browser             iomenu              smtplib
_collections        builtins            ipaddress           sndhdr
_collections_abc    bz2                 itertools           socket
_compat_pickle      cProfile            json                socketserver
_compression        calendar            keyword             sqlite3
_contextvars        calltip             lib2to3             squeezer
_csv                calltip_w           linecache           sre_compile
_ctypes             cgi                 locale              sre_constants
_ctypes_test        cgitb               logging             sre_parse
_datetime           chunk               lzma                ssl
_decimal            cmath               macosx              stackviewer
_distutils_hack     cmd                 mailbox             stat
_elementtree        code                mailcap             statistics
_functools          codecontext         mainmenu            statusbar
_hashlib            codecs              marshal             string
_heapq              codeop              math                stringprep
_imp                collections         mimetypes           struct
_io                 colorizer           mmap                subprocess
_json               colorsys            modulefinder        sunau
_locale             compileall          msilib              symtable
_lsprof             concurrent          msvcrt              sys
_lzma               config              multicall           sysconfig
_markupbase         config_key          multiprocessing     tabnanny
_md5                configdialog        netrc               tarfile
_msi                configparser        nntplib             telnetlib
_multibytecodec     contextlib          nt                  tempfile
_multiprocessing    contextvars         ntpath              test
_opcode             copy                nturl2path          textview
_operator           copyreg             numbers             textwrap
_osx_support        crypt               opcode              this
_overlapped         csv                 operator            threading
_pickle             ctypes              optparse            time
_py_abc             curses              os                  timeit
_pydecimal          dataclasses         outwin              tkinter
_pyio               datetime            parenmatch          token
_queue              dbm                 pathbrowser         tokenize
_random             debugger            pathlib             tooltip
_sha1               debugger_r          pdb                 trace
_sha256             debugobj            percolator          traceback
_sha3               debugobj_r          pickle              tracemalloc
_sha512             decimal             pickletools         tree
_signal             delegator           pip                 tty
_sitebuiltins       difflib             pipes               turtle
_socket             dis                 pkg_resources       turtledemo
_sqlite3            distutils           pkgutil             types
_sre                doctest             platform            typing
_ssl                dynoption           plistlib            undo
_stat               editor              poplib              unicodedata
_statistics         email               posixpath           unittest
_string             encodings           pprint              urllib
_strptime           ensurepip           profile             util
_struct             enum                pstats              uu
_symtable           errno               pty                 uuid
_testbuffer         faulthandler        py_compile          venv
_testcapi           filecmp             pyclbr              warnings
_testconsole        fileinput           pydoc               wave
_testimportmultiple filelist            pydoc_data          weakref
_testinternalcapi   fnmatch             pyexpat             webbrowser
_testmultiphase     format              pyparse             window
_thread             fractions           pyshell             winreg
_threading_local    ftplib              query               winsound
_tkinter            functools           queue               wsgiref
_tracemalloc        gc                  quopri              xdrlib
_uuid               genericpath         random              xml
_warnings           getopt              re                  xmlrpc
_weakref            getpass             redirector          xxsubtype
_weakrefset         gettext             replace             zipapp
_winapi             glob                reprlib             zipfile
_xxsubinterpreters  graphlib            rlcompleter         zipimport
_zoneinfo           grep                rpc                 zlib
abc                 gzip                run                 zoneinfo
aifc                hashlib             runpy               zoomheight
antigravity         heapq               runscript           zzdummy

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> exit
Help on Quitter in module _sitebuiltins object:

exit = class Quitter(builtins.object)
 |  exit(name, eof)
 |  
 |  Methods defined here:
 |  
 |  __call__(self, code=None)
 |      Call self as a function.
 |  
 |  __init__(self, name, eof)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __repr__(self)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
#
# this is comment
print (" hello i am your python buddy")
 hello i am your python buddy
print ("did you know /n me ?")
did you know /n me ?
print (" did you know \n me ? ")
 did you know 
 me ? 
a,b = 2,4
print(a,b)
2 4
print(*"lets hack")
l e t s   h a c k
a=10
id(a)
2260192395792
a=9
id(a)
2260192395760
a = input("enter your name")
enter your namehet
a
'het'
a= int(input("entre a value"))
entre a value10
a
10
type(a)
<class 'int'>
a=2
b=3
print(a,b,sep='%')
2%3
