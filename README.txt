------------------------------------
/            Welcome               /
/   to my first completed project  /
/      By: moustafa.py             /
------------------------------------

DISCLAIMER:
Make sure that after every equal click, you first clear (not back) the display then you can make another calculation. And
make sure to place a 0 before you write in a float number.


Anyways,

This is a very silly, poorly written, and simple project. But making this project marks my transition from
tutorial purgatory to actually finishing a project and making progress with my coding. I just got back into
programming after 7 years of not practicing, and I have so much to learn and room for improvement, and I hope
I can look back at this project and see how much progress I (hopefully) have made. Hopefully by the time I
finish college my proficiency in coding can open doors career wise.

I started by using tkinter, tkinter is fine but I found I was not proficient enough in tkinter
to make a calculator with it. I found that using QTdesigner was easier, but I still had the issue of functionality
with my calculator. At first, like I tried with my tkinter prototype, I decided to make a bunch of variables and
change these variables when the buttons are pressed. I had a function for each button process, with the number keys
having their own function and the operations utilizing their own individual functions. I ended up with such spaghetti code
that froze me on debugging and writing on top of this code. This rather simple project still showed me how important basic
software design is for making code clean and scalable. In addition, I still wasn't able to actually make the calculator
function and solve arithmetic.

On the toilet one day I discovered the obvious, why not make the display show a string
that I can change with button clicks, then evaluate that string by pressing equal? The problem was is that
the eval() function is a security issue that I was not well versed in, thus I had to find a different option. I found that
the pyparsing module was a safer alternative to eval(), which I found via stackoverflow. I was particularly happy with
this solution (despite how buggy this calculator actually is) just because of the fact that I actually had to "think
like a programmer" and come up with a novel solution. Of course this solution is very flawed and not ideal, but its
progress at least.

If you have any suggestions to fix my code, please let me know and make a commit. I'd like to learn more and improve on
my mistakes, and become a better programmer.
