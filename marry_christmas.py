import time

lines = [
    "  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *",
    "*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *",
    "  *  *  *  *  *  ||\\    /|| ||\\\\\\\\ ||\\\\\   ||\\\\\  \\\\  //   *  *  *  *  *",
    "*  *  *  *  *  * ||\\\\  //|| ||     ||  ||  ||  ||  \\\\//  *  *  *  *  *  *",
    "  *  *  *  *  *  || \\\\// || ||\\\\\  ||///   ||///    \/  *  *  *  *  *  *",
    "*  *  *  *  *  * ||      || ||     || \\\\   || \\\    ||   *  *  *  *  *  *",
    "  *  *  *  *  *  ||      || ||\\\\\\\\ ||  \\\\  ||  \\\\   ||  *  *  *  *  *  *",
    "*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *",
    "  ///\\\\  ||   || ||\\\\\  ||  ///\\\\ |||||||| ||\    /||     /\\      ///\\\\",
    "*||   \\\\ ||   || ||  || || //        ||    ||\\\\  //||    //\\\\    //     *",
    " ||      ||||||| ||///  ||  \\\\\\\\     ||    || \\\\// ||   //  \\\\    \\\\\\\\",
    "*||   // ||   || || \\\\  ||     //    ||    ||      ||  //||||\\\\      // *",
    "  \\\\\//  ||   || ||  \\\\ || \\\\///     ||    ||      || //      \\\\ \\\\/// ",
    "*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *",
    "  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *",
]
pause = 0.5
for line in lines:
    print(line)
    time.sleep(pause)
