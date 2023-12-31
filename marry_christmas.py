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


def draw_tree(size: int):
    for i in range(1, size):
        tree_rows = 8*((size-i)*" "+(2*i-1)*"*"+(size-i)*" ")
        print(tree_rows)
    tree_trunks = 8*((size-1)*" "+"|"+(size-1)*" ")
    print(tree_trunks)


draw_tree(5)

pause = 0.5
for line in lines:
    print(line)
    time.sleep(pause)
