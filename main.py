from view import View
from model import Model
from controller import Controller

if __name__ == "__main__":
    model = Model(None)
    controller = Controller(None, model)
    view = View(controller)

    controller.view = view
    model.controller = controller

    view.start()