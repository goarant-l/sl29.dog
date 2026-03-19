from sl29.dog import Dog


# Exemple d'utilisation
rin = Dog(race="Berger allemand", sex="M", name="Rintintin")
rine = Dog(race="Berger allemand", sex="F", name="Rintintine")
chiot = rin.mate(rine)
