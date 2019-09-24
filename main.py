import difficulty as diff
import numpy as np
import matplotlib.pyplot as plt


def main():
    test1D()


def test1D():
    minute_time = 25
    stage_time = 5

    xs = np.arange(0, minute_time, 1)
    ys = diff.coeff(xs, stage_time, 1, diff.MONSOON)

    plt.title('Coeff vs time for {} min stage avg'.format(stage_time))
    plt.xlabel('Time (min)')
    plt.ylabel('Difficulty Coefficient')
    plt.plot(xs, ys)
    plt.show()



if __name__ == '__main__':
    main()
