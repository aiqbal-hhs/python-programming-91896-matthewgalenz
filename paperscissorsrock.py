hand = randint(0, 2)
if hand == 0:
    basic.show_leds("""
        . # # # .
        # # # # #
        # # # # #
        # # # # #
        . # # # .
        """)
elif hand == 1:
    basic.show_leds("""
        # # . . #
        # # . # .
        . # # . .
        # # . # .
        # # . . #
        """)
else:
    basic.show_leds("""
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        """)
