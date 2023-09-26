from notes.idea import Idea


class Ideas:
    __ideas: dict = {}

    @classmethod
    def dict_ideas(cls):
        return cls.__ideas

    @classmethod
    def add_idea(cls, idea: Idea):
        cls.__ideas[idea.id] = idea.text

    @classmethod
    def get_new_id(cls):
        return str(len(cls.__ideas)+1)

    @classmethod
    def edit_idea(cls, id: str, text: str):
        cls.__ideas[id] = text
