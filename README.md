# Just the snippets of man you want

Man pages are an impressive feat. Some of them are very large and hard to navigate.

For instance, let's say I was looking for the syntax for the built-in declare command inside of bash.

I would do

    $ man bash

Then just search for declare

Here's the problem:

    $ man bash | grep -c declare
    34

There's 34 of them.

## Wouldn't it be nice to just get the part you want?

Yes, why does this not exist? Why can't I just do something like this?

    $ man bash | mansnip declare
           declare [-aAfFgilnrtux] [-p] [name[=value] ...]
           typeset [-aAfFgilnrtux] [-p] [name[=value] ...]
                  Declare variables and/or give them attributes.  If no names are given then display the
                  values  of  variables.   The  -p option will display the attributes and values of each
                  name.  When -p is used with name arguments, additional options, other than -f and  -F,
                  are  ignored.   When  -p  is  supplied without name arguments, it will display the at‐
                  tributes and values of all variables having the attributes specified by the additional
                  options.   If  no  other  options  are  supplied with -p, declare will display the at‐
                  tributes and values of all shell variables.  The -f option will restrict  the  display
                  to  shell functions.  The -F option inhibits the display of function definitions; only
                  the function name and attributes are printed.  If the extdebug shell option is enabled
                  using  shopt, the source file name and line number where each name is defined are dis‐
           ...
    $

Well, now you can! (ok that was obvious, that's why I'm talking about it)

## Why hasn't this existed forever?

Well, man pages don't really encode a lot of semantic detail. The man format is pretty old. There's been a number of replacements, such as GNU info and BSD mandoc but the ones you have on your system are probably boring old man files.

Being old, it's primarily concerned with formatting and not any kind of meta-information. And boy can it format! Try using the groffer(1) tool and do something like `groffer ffmpeg`. You'll hopefully get a very beautiful PDF popping up on your screen, excellent for printing out and keeping in a 3-ring binder next to your rolodex and fax machine.

Inside the source itself, however, there is next to no indication that something is special. Let's go back to bash and specifically the lines that say "declare" and "typeset". Here's the actual source:

    .TP
    \fBdeclare\fP [\fB\-aAfFgilnrtux\fP] [\fB\-p\fP] [\fIname\fP[=\fIvalue\fP] ...]
    .PD 0
    .TP
    \fBtypeset\fP [\fB\-aAfFgilnrtux\fP] [\fB\-p\fP] [\fIname\fP[=\fIvalue\fP] ...]
    .PD

Alright, what do those things mean? You can see that in `man 7 man` or actually, 

    $  man 7 man | mansnip .TP .PD 
       .TP i    Begin paragraph with hanging tag.  The tag is given on the next line,  but  its  re‐
                sults are like those of the .IP command.
       .PD d    Set  inter-paragraph  vertical  distance to d (if omitted, d=0.4v); does not cause a
                break.

Hrmm, well that's a problem. It's effectively just a style-sheet.

"But wait," you say. "If I do man -html bash and then wait for the glacially slow groff html post processor I do indeed get links!"

Yes, the only two semantic concessions given in the man format is `.SH` which is for sections and `.TH` for the title.

"So there's no surefire easy way to do this, you can only guess?"

Uh, yep, lol.


### It's not that terrible though

Man pages are ridiculously consistent as far as non-semantically structured text goes.  It seems to work fine and if it doesn't, you can just go hunting and pecking like you usually do.

### This code looks really simple

Yeah, not everything that's useful is necessarily hard.

