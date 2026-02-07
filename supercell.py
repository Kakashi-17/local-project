#SUPERCELL PROJECT USING DICT METHOD 

# def clash_of_clans(spells_name):
#     spells = {
#         "Lightning" : dict(
#             spell_name = "Lightning Spell",
#             work = "Use to destroy Air Defenses or weaken strong defenses.",
#             uses = "Destroy Air Defenses, Mortars, or Clan Castle troops.",
#         ),
#         "Healing" : dict(
#             spell_name = "Healing Spell",
#             work = "Makes a yellow circle that heals your troops inside it ",
#             uses = "Use to keep Hogs, Miners, or Balloons alive longer.",
#         ),
#         "Rage" : dict(
#             spell_name = "Rage Spell",
#             work = "Makes troops move faster and hit harder inside the purple circle. ",
#             uses = "Use when troops reach the core or strong defenses " ,
#         ),
#         "Jump" : dict(
#             spell_name = "Jump Spell",
#             work = "Lets your ground troops jump over walls.",
#             uses = "Use to help troops move quickly into enemy base",
#         ),
#         "Freeze" : dict(
#             spell_name = "Freeze Spell",
#             work = "Use to freeze Inferno Towers, Eagle Artillery, or Scattershots.",
#             uses =	"Stops defenses and heroes for a short time.",
#         ),
#         "Clone" : dict(
#             spell_name = "Clone Spell",
#             work = "Makes extra copies of your troops for a short time.",
#             uses = "Use with Balloons, Electro Dragons, or other strong troops."
#         ),
#         "Invisibility" : dict(
#             spell_name = "Invisibility Spell",	
#             work = "Makes troops or buildings invisible for a short time.",
#             uses = "Use to protect heroes or Blimps during attacks."
#         ),
#         "Poison" : dict(
#             spell_name = "Poison Spell",
#             work = "Creates a dark circle that slows and hurts enemy troops.",
#             uses = "Use against enemy Clan Castle troops or heroes."
#         ),
#         "Earthquake" : dict(
#             spell_name = "Earthquake Spell",
#             work = "Shakes the ground and damages buildings and walls.",
#             uses = "Use to open walls or weaken strong defenses."
#         ),
#         "Haste" : dict(
#             spell_name = "Haste Spell",
#             work = "Makes troops move very fast (no extra damage).",
#             uses = "Use with Balloons or Minions to reach defenses faster."
#         ),
#         "Skeleton" : dict(
#             spell_name = "Skeleton Spell",
#             work = "Summons many skeletons that attack nearby targets.",
#             uses = "Use to distract defenses or help kill heroes."   
#         ),
#         "Bat" : dict(
#             spell_name = "Bat Spell",
#             work = "Summons bats that attack defenses.",
#             uses = "Use after freezing splash defenses (like Wizard Towers)."
#         )    
#     }
#     spell_name = spells_name.title()
#     return spells.get(spell_name,dict("ERROR : spell not found. Please enter a valid coc spell name"))

# spells_name = input("Enter spell name : ")
# info = clash_of_clans(spells_name)


# SUPERCELL PROJECT USING OOPS METHOD 
class Spell:
    def __init__(self, name, work, uses):
        self.name = name
        self.work = work
        self.uses = uses

    def display_info(self):
        print(f"\n Spell : {self.name}")
        print(f" Work : {self.work}")
        print(f" Uses : {self.uses}")
        print("---" * 25)


class SpellBook:
    def __init__(self):
        self.spells = {
            "Lightning": Spell(
                "Lightning Spell",
                "Use to destroy Air Defenses or weaken strong defenses.",
                "Destroy Air Defenses, Mortars, or Clan Castle troops.",
            ),
            "Healing": Spell(
                "Healing Spell",
                "Makes a yellow circle that heals your troops inside it.",
                "Use to keep Hogs, Miners, or Balloons alive longer.",
            ),
            "Rage": Spell(
                "Rage Spell",
                "Makes troops move faster and hit harder inside the purple circle.",
                "Use when troops reach the core or strong defenses.",
            ),
            "Jump": Spell(
                "Jump Spell",
                "Lets your ground troops jump over walls.",
                "Use to help troops move quickly into enemy base.",
            ),
            "Freeze": Spell(
                "Freeze Spell",
                "Use to freeze Inferno Towers, Eagle Artillery, or Scattershots.",
                "Stops defenses and heroes for a short time.",
            ),
            "Clone": Spell(
                "Clone Spell",
                "Makes extra copies of your troops for a short time.",
                "Use with Balloons, Electro Dragons, or other strong troops.",
            ),
            "Invisibility": Spell(
                "Invisibility Spell",
                "Makes troops or buildings invisible for a short time.",
                "Use to protect heroes or Blimps during attacks.",
            ),
            "Poison": Spell(
                "Poison Spell",
                "Creates a dark circle that slows and hurts enemy troops.",
                "Use against enemy Clan Castle troops or heroes.",
            ),
            "Earthquake": Spell(
                "Earthquake Spell",
                "Shakes the ground and damages buildings and walls.",
                "Use to open walls or weaken strong defenses.",
            ),
            "Haste": Spell(
                "Haste Spell",
                "Makes troops move very fast (no extra damage).",
                "Use with Balloons or Minions to reach defenses faster.",
            ),
            "Skeleton": Spell(
                "Skeleton Spell",
                "Summons many skeletons that attack nearby targets.",
                "Use to distract defenses or help kill heroes.",
            ),
            "Bat": Spell(
                "Bat Spell",
                "Summons bats that attack defenses.",
                "Use after freezing splash defenses (like Wizard Towers).",
            ),
        }

    def get_spell(self, name):
        spell_name = name.title()
        return self.spells.get(spell_name, None)



if __name__ == "__main__":
    spellbook = SpellBook()
    spell_name = input("Enter spell name: ")
    spell = spellbook.get_spell(spell_name)

    if spell:
        spell.display_info()
    else:
        print(" ERROR: Spell not found. Please enter a valid Clash of Clans spell name.")