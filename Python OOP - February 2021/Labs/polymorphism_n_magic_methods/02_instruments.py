def play_instrument(instance):
    return instance.play()


class Piano:
    def play(self):
        print("playing the piano")
piano = Piano()
play_instrument(piano)
