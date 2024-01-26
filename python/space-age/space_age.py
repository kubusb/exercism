class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        earth_year_in_seconds = 31557600
        age_on_earth = self.seconds / earth_year_in_seconds
        return round(age_on_earth, 2)

    def on_venus(self):
        venus_year_in_seconds = 0.61519726 * 31557600
        age_on_venus = self.seconds / venus_year_in_seconds
        return round(age_on_venus, 2)

    def on_jupiter(self):
        jupiter_year_in_seconds = 11.862615 * 31557600
        age_on_jupiter = self.seconds / jupiter_year_in_seconds
        return round(age_on_jupiter, 2)

    def on_mars(self):
        mars_year_in_seconds = 1.8808158 * 31557600
        age_on_mars = self.seconds / mars_year_in_seconds
        return round(age_on_mars, 2)

    def on_mercury(self):
        mercury_year_in_seconds = 0.2408467 * 31557600
        age_on_mercury = self.seconds / mercury_year_in_seconds
        return round(age_on_mercury, 2)

    def on_neptune(self):
        neptune_year_in_seconds = 164.79132 * 31557600
        age_on_neptune = self.seconds / neptune_year_in_seconds
        return round(age_on_neptune, 2)

    def on_saturn(self):
        saturn_year_in_seconds = 29.447498 * 31557600
        age_on_saturn = self.seconds / saturn_year_in_seconds
        return round(age_on_saturn, 2)

    def on_uranus(self):
        uranus_year_in_seconds = 84.016846 * 31557600
        age_on_uranus = self.seconds / uranus_year_in_seconds
        return round(age_on_uranus, 2)
