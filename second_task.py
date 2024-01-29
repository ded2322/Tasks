class City:
    def __init__(self, name, antagonist):
        self.name = name
        self.antagonist = antagonist

    def get_threat(self):
        return f"{self.antagonist} stands near a skyscraper in {self.name}"


class Superhero:
    def __init__(self, name, attack_style):
        self.name = name
        self.attack_style = attack_style

    def attack(self):
        return f"{self.attack_style}"


class Media:
    def broadcast(self, message):
        raise NotImplementedError("Broadcast method should be implemented")


class Newspaper(Media):
    def broadcast(self, message):
        return f"Today in newspapers: {message}"


class Television(Media):
    def broadcast(self, message):
        return f"Watch on the first channel: {message}"


class Battle:
    def __init__(self, superhero, city, media):
        self.superhero = superhero
        self.city = city
        self.media = media

    def fight(self):
        threat = self.city.get_threat()
        attack = self.superhero.attack()
        result = f"{self.superhero.name} saved {self.city.name}!"
        broadcast_message = self.media.broadcast(result)

        return f"{threat}\n{attack}\n{broadcast_message}"


# Пример использования
city = City("Tokyo", "Godzilla")
superhero = Superhero("Chuck Norris", "PIU PIU")
media = Television()

battle = Battle(superhero, city, media)
print(battle.fight())