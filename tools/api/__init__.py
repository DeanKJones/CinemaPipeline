from engine.base_engine import Engine


def open(path):
    current_engine = Engine.get_engine()
    current_engine.open(path)


def save():
    current_engine = Engine.get_engine()
    current_engine.save()

