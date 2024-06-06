import matplotlib.pyplot as plot

class SoundWave:
    def show(wave):
        # Plot a sine wave using time and amplitude obtained for the sine wave

        plot.plot(wave)

        # Give a title for the sine wave plot

        plot.title('Sound')

        # Give x axis label for the sine wave plot

        plot.xlabel('Time')

        # Give y axis label for the sine wave plot

        plot.ylabel('Amplitude')

        plot.grid(True, which='both')

        plot.axhline(y=0, color='k')

        plot.show()