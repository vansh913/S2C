from dataclasses import dataclass, field
from typing import Dict
import os
import spacy

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

def parse_story(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    characters = {}  # dict of name: {'attrs': []}
    dialogues = []  # list of (speaker, text, sent_index)
    for i, sent in enumerate(sentences):
        # Simple dialogue detection: look for quotes
        if '"' in sent:
            parts = sent.split('"')
            if len(parts) >= 3:
                speaker_part = parts[0].strip()
                dialogue = parts[1]
                # Assume speaker is the last word before quote
                speaker = speaker_part.split()[-1] if speaker_part else None
                dialogues.append((speaker, dialogue, i))
                if speaker and speaker not in characters:
                    characters[speaker] = {'attrs': []}
        # Extract characters as PERSON entities
        sent_doc = nlp(sent)
        for ent in sent_doc.ents:
            if ent.label_ == 'PERSON':
                name = ent.text
                if name not in characters:
                    characters[name] = {'attrs': []}
    return sentences, characters, dialogues
