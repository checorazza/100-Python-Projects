from expert import OrderProcessingExpert

class OrderProcessingContext:
    def __init__(self):
        self.experts = []

    def add_expert(self, expert: OrderProcessingExpert):
        self.experts.append(expert)

    def process_order(self, order):
        for expert in self.experts:
            expert.process(order)
