from dataclasses import dataclass, field
from typing import Dict
import os

@dataclass
class CharacterProfile:
    name: str
    attrs: list = field(default_factory=list)
    ref_image_path: str = None

class CharacterDictionary:
    def __init__(self):
        self.characters: Dict[str, CharacterProfile] = {}

    def add_or_update(self, name, attrs=None):
        if name not in self.characters:
            self.characters[name] = CharacterProfile(name=name, attrs=attrs or [])
        else:
            if attrs:
                for a in attrs:
                    if a not in self.characters[name].attrs:
                        self.characters[name].attrs.append(a)

    def set_ref_image(self, name, path):
        if name in self.characters:
            self.characters[name].ref_image_path = path

    def __iter__(self):
        return iter(self.characters.items())
