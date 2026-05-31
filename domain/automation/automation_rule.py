class AutomationRule:

    def __init__(self, trigger, action):

        self._trigger = trigger
        self._action = action
        self._active = True

    def matches(self, event):

        return self._active and event == self._trigger

    def execute(self):

        self._action()

    def deactivate(self):
        self._active = False

    def activate(self):
        self._active = True