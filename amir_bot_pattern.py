# amir_bot_pattern_v2.py - Edition "Même Meme Depuis 2022" 
# Plus prévisible qu'un NPC de GTA San Andreas, plus cringe qu'un TikTok 2019

import random
import time
import sys
from datetime import datetime

class AmirBotV2:
    def __init__(self):
        self.emotes = ["🤡", "L", "💀", "😭", "🤡", "🔥", "🗿", "cope", "ratio", "seethe", "💀", "🤡"]
        self.meme_spam = "https://i.imgur.com/leMemeMortDeAmir.jpg"  # ← remplace par LE vrai lien qu'il spam H24
        self.phrases_pretentieuses = [
            "Vous êtes tous des noobs, moi je suis le goat depuis 2018",
            "Erreur ? C'est votre PC patate, pas mon skill",
            "Je carry cette voc, sans moi vous seriez en train de jouer à Among Us",
            "Je ragequit pas, je fais une pause stratégique",
            "Rejoignez-moi les bg ou restez dans le lobby des losers",
            "Mon humour est trop avancé pour vous",
            "GTA 6 retardé à cause de vous, pas moi"
        ]
        self.habitudes = [
            "rejoint la voc",
            "quitte à cause d'une 'erreur'",
            "spam emotes random",
            "envoie LE même meme cringe",
            "ragebait en 2-4 messages",
            "se la pète niveau Dieu"
        ]
        self.meme_count = 0
        self.rage_level = 0
        self.cringe_meter = 0

    def print_header(self):
        now = datetime.now().strftime('%H:%M:%S')
        print(f"[{now}] AmirBot v2.0 - Cycle #{self.cringe_meter + 1} | Cringe: {self.cringe_meter}/100 | Rage: {self.rage_level}")

    def spam_meme(self):
        self.meme_count += 1
        self.cringe_meter += 3
        print(f"Amir balance SON meme pour la {self.meme_count}ème fois : {self.meme_spam}")
        print("   (tout le monde : 💀 silence gênant 💀)")
        if self.meme_count % 5 == 0:
            print("   → Même les bots Discord ont bloqué ce lien")

    def simulate_cycle(self):
        self.print_header()

        action = random.choices(
            self.habitudes,
            weights=[20, 25, 15, 18, 12, 10],  # plus de poids sur quit + meme spam
            k=1
        )[0]

        if action == "rejoint la voc":
            print("➜ Amir rejoint la voc... fidèle au poste comme un stalker")
            time.sleep(random.uniform(1.2, 2.8))

        elif action == "quitte à cause d'une 'erreur'":
            self.rage_level += 15
            print("⚠️ 'Erreur fatale' (ping +12ms = world end)")
            print(f"Amir ragequit en {random.uniform(0.4, 1.1):.2f} secondes - record battu ?")
            time.sleep(1.8)

        elif action == "spam emotes random":
            spam = " ".join(random.sample(self.emotes, k=random.randint(5, 12)))
            print(f"Amir spam emotes : {spam}")
            self.cringe_meter += 2
            time.sleep(0.9)

        elif action == "envoie LE même meme cringe":
            self.spam_meme()
            time.sleep(random.uniform(1.5, 3.5))

        elif action == "ragebait en 2-4 messages":
            phrase = random.choice(self.phrases_pretentieuses)
            print(f"Amir : \"{phrase}\"")
            print("   ...attente du premier qui répond pour tilt...")
            time.sleep(random.uniform(2.5, 5.0))
            self.rage_level += 8

        elif action == "se la pète niveau Dieu":
            print("Amir : \"Franchement sans moi cette voc serait morte depuis longtemps\"")
            self.cringe_meter += 5
            time.sleep(2.2)

        # Les potes zombies reviennent toujours
        print("   ↳ Les 3 mêmes moutons re-re-rejoignent en mode autopilot")

        # Check si trop cringe ou trop rage → crash épique
        if self.cringe_meter >= 80 or self.rage_level >= 70:
            print("\n" + "="*60)
            print("AMIR OVERLOAD : Trop de cringe + rage = serveur en PLS")
            print(f"Stats finales → Mèmes spammés : {self.meme_count} | Cringe : {self.cringe_meter} | Rage : {self.rage_level}")
            print("Il va revenir dans 4min en mode \"c'était pour rire\" 😂")
            print("="*60 + "\n")
            sys.exit(69)  # exit code cringe

    def run(self):
        print("=== SIMULATEUR AMIR v2.0 - Mode Infini Cringe activé ===")
        print(f"Meme signature d'Amir : {self.meme_spam}")
        print("Prédiction : 100% des actions = hier = avant-hier = 2021\n")

        try:
            while True:
                self.simulate_cycle()
                time.sleep(random.uniform(2.0, 6.0))  # temps entre cycles = drama cooldown
        except KeyboardInterrupt:
            print("\nT'as ragequit le simu Amir ? T'es officiellement plus fort que lui 😭")

if __name__ == "__main__":
    bot = AmirBotV2()
    bot.run()
