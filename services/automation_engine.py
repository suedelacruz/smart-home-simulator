class AutomationEngine:

    def __init__(self):

        self._rules = []

    def add_rule(self, rule):

        self._rules.append(rule)

    def update(self, event):

        self.process_event(event)

    def process_event(self, event):

        print(f"[EVENT] {event}")

        for rule in self._rules:

            if rule.matches(event):

                rule.execute()