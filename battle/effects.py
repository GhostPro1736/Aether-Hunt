from .attacks import Effect,Attacks
burn = Effect(name="burn", effect_type="fire", target="enemy")
paralisation = Effect(name="paralisation", effect_type="electric", target="enemy", priority=2, max_duration=5)
fireball = Attacks(damage=10, type="aura", name="fireball", effects=[burn])
fireball.add_effect_attributes(effect_name="burn", effect_duration=3, damage=10)