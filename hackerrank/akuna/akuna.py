"""
Designing a market position monitor for a stock.

Run by passing the input* file in tests/ as run time argument
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Hackerrank.com","akunacapital"]
__status__  = "Prototype"


import json
import sys

class MarkingPositionMonitor:
    def __init__(self):
        self.marking_position = {}
        self.order_info = {}
    
    def on_event(self, message):
        message_dict = json.loads(message)
        
        if message_dict['type'] == 'NEW':
            self.process_new(message_dict)
            
        order_id = message_dict['order_id']
        first_message = self.order_info[order_id]
        symbol = first_message['symbol']
        
        if message_dict['type'] == 'CANCEL_ACK':
            self.process_cancel_ack(order_id,symbol)
            
        if message_dict['type'] == 'ORDER_REJECT':
            self.process_order_reject(order_id,symbol)
            
        if message_dict['type'] == 'FILL':
            filled_quantity = message_dict['filled_quantity']
            remaining_quantity = message_dict['remaining_quantity']
            self.process_fill(order_id,symbol,filled_quantity,remaining_quantity)
            
        #if message_dict['type'] == 'ORDER_ACCEPT':
            #self.process_order_accept(order_id,symbol)
            
        return self.marking_position[symbol]
    
    def process_new(self,message):
        self.order_info[message['order_id']] = message
        if message['symbol'] not in self.marking_position:
            self.marking_position[message['symbol']] = 0
            
        if message['side'] == 'SELL':
            self.marking_position[message['symbol']] -= message['quantity']
            
    def process_cancel_ack(self,order_id,symbol):
        
        order = self.order_info[order_id]
        
        if order['side'] == 'SELL':
            self.marking_position[symbol] += order['quantity']
            
    def process_order_reject(self,order_id,symbol):
        order = self.order_info[order_id]
        
        if order['side'] == 'SELL':
            self.marking_position[symbol] += order['quantity']
    
    
    def process_fill(self,order_id,symbol,filled_quantity,remaining_quantity):
        order = self.order_info[order_id]
        
        if order['side'] == 'BUY':
            self.marking_position[symbol] += filled_quantity
            
        order['quantity'] = remaining_quantity


if __name__== '__main__':
    m = MarkingPositionMonitor()
    with open(sys.argv[1],'r') as fd:
        for line in fd:
            print(m.on_event(line))
