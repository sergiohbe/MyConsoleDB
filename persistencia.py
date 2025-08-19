from pymongo import MongoClient

class Mongo:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client["MyConsoleDb"]
        self.col = self.db["listas"]

        self.catalog = self.db["catalogo_consoles"]

        consoles = [
            {"nome": "Playstation"},
            {"nome": "Playstation 2"},
            {"nome": "Playstation 2 Slim"},
            {"nome": "Playstation 3"},
            {"nome": "Playstation 3 Slim"},
            {"nome": "Playstation 3 Super Slim"},
            {"nome": "Playstation 4"},
            {"nome": "Playstation 4 Slim"},
            {"nome": "Playstation 4 Pro"},
            {"nome": "Playstation 5"},
            {"nome": "Playstation 5 Slim"},
            {"nome": "Playstation 5 Pro"},
            {"nome": "Xbox"},
            {"nome": "Xbox 360"},
            {"nome": "Xbox 360 Elite"},
            {"nome": "Xbox 360 Slim"},
            {"nome": "Xbox 360 Super Slim"},
            {"nome": "Xbox One"},
            {"nome": "Xbox One Elite"},
            {"nome": "Xbox One S"},
            {"nome": "Xbox One X"},
            {"nome": "Xbox Series S"},
            {"nome": "Xbox Series X"},
            {"nome": "SG-1000"},
            {"nome": "Sega Mark III"},
            {"nome": "Master System"},
            {"nome": "Mega Drive (Genesis)"},
            {"nome": "Game Gear"},
            {"nome": "Sega Pico"},
            {"nome": "Sega Saturn"},
            {"nome": "Dreamcast"},
            {"nome": "Color TV-Game"},
            {"nome": "Nintendo Entertainment System (NES)"},
            {"nome": "Game Boy"},
            {"nome": "Super Nintendo Entertainment System (SNES)"},
            {"nome": "Virtual Boy"},
            {"nome": "Nintendo 64"},
            {"nome": "Game Boy Color"},
            {"nome": "Game Boy Advance"},
            {"nome": "Nintendo GameCube"},
            {"nome": "Nintendo DS"},
            {"nome": "Wii"},
            {"nome": "Nintendo 3DS"},
            {"nome": "Wii U"},
            {"nome": "Nintendo Switch"},
            {"nome": "Nintendo Switch Lite"},
            {"nome": "Nintendo Switch Oled"},                        
            {"nome": "Atari 2600"},
            {"nome": "Atari 5200"},
            {"nome": "Atari 7800"},
            {"nome": "Atari Lynx"},
            {"nome": "Atari Jaguar"},
            {"nome": "Zeebo"}
        ]
        
        if self.catalog.count_documents({}) == 0:
            self.catalog.insert_many(consoles)

    def get_catalogo(self):
        return [doc["nome"] for doc in self.db["catalogo_consoles"].find()]

    def salvar_listas(self, own, had, wish):
        self.col.delete_many({})
        self.col.insert_one({
            "own": own,
            "had": had,
            "wish": wish
        })

    def carregar_listas(self):
        x = self.col.find_one()
        if x:
            return x.get("own", []), x.get("had", []), x.get("wish", [])
        return [], [], []