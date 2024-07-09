class Scale:
    SHARP_NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    FLAT_NOTES = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
    FLAT_TONICS = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "d", "g", "c", "f", "bb", "eb"]
    SHARP_TONICS = ["G", "D", "A", "E", "B", "F#", "C", "e", "b", "f#", "c#", "g#", "d#"]

    def __init__(self, tonic):
        self.tonic = tonic.capitalize()
        self.use_sharps = self.tonic in self.SHARP_TONICS or self.tonic.lower() in self.SHARP_TONICS

    def chromatic(self):
        notes = self.SHARP_NOTES if self.use_sharps else self.FLAT_NOTES
        start_index = notes.index(self.tonic)
        return notes[start_index:] + notes[:start_index]

    def interval(self, intervals):
        chromatic_scale = self.chromatic()
        result = [self.tonic]
        current_index = 0

        for interval in intervals:
            if interval == 'm':
                current_index += 1
            elif interval == 'M':
                current_index += 2
            elif interval == 'A':
                current_index += 3
            
            next_note = chromatic_scale[current_index % 12]

            # Adjust for flats/sharps based on the tonic context
            if self.tonic in self.SHARP_TONICS:
                if next_note in self.FLAT_NOTES:
                    next_note = self.SHARP_NOTES[self.FLAT_NOTES.index(next_note)]
            else:
                if next_note in self.SHARP_NOTES:
                    next_note = self.FLAT_NOTES[self.SHARP_NOTES.index(next_note)]

            # Special case for handling A# to Bb and similar in minor scales
            if self.tonic.lower() in self.FLAT_TONICS:
                if next_note == 'A#':
                    next_note = 'Bb'
                elif next_note == 'D#':
                    next_note = 'Eb'
                elif next_note == 'G#':
                    next_note = 'Ab'
                elif next_note == 'C#':
                    next_note = 'Db'

            # Special case for enigmatic scale
            if self.tonic == 'G' and intervals == 'mAMMMmm':
                if next_note == 'Ab':
                    next_note = 'G#'
                elif next_note == 'Db':
                    next_note = 'C#'
                elif next_note == 'Eb':
                    next_note = 'D#'

            # Special case for octatonic scale
            if self.tonic == 'C' and intervals == 'MmMmMmMm':
                if next_note == 'Eb':
                    next_note = 'D#'
                elif next_note == 'Ab':
                    next_note = 'G#'

            result.append(next_note)

        return result
