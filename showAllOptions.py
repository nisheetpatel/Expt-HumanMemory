from psychopy import visual, event, core
from expt.options import create_choice_options

if __name__ == "__main__":
    # creating the experiment
    # create window
    win = visual.Window([1024, 768], fullscr=False, units="pix")

    # create probe stimuli
    all_choice_options = create_choice_options(win=win)
    all_choice_options = all_choice_options[:12]

    # defining positions of all options
    x_pos_1 = 300
    x_pos_2 = 100
    y_pos = 200
    positions = [
        [-x_pos_1, y_pos],
        [-x_pos_1, 0],
        [-x_pos_1, -y_pos],
        [-x_pos_2, y_pos],
        [-x_pos_2, 0],
        [-x_pos_2, -y_pos],
        [x_pos_2, y_pos],
        [x_pos_2, 0],
        [x_pos_2, -y_pos],
        [x_pos_1, y_pos],
        [x_pos_1, 0],
        [x_pos_1, -y_pos],
    ]

    # drawing all the options on the window
    for option, pos in zip(all_choice_options, positions):
        option.shape.setPos(newPos=pos)
        option.shape.draw()
    win.flip()

    # quit window when user presses escape
    keys = event.waitKeys(keyList=["escape"])
    core.quit()
