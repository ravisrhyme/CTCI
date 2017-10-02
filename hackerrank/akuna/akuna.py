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

# Implement the class below, keeping the constructor's signature unchanged; it should take no arguments.

class MarkingPositionMonitor:
    def __init__(self):
        self.marking_position = {}
        self.order_info = {}
    
    def on_event(self, message):
        "Returns the marking position monitor for a symbol"
        message = json.loads(message)
        if message["type"] == 'NEW':
            self.process_new(message)

        order_id = message['order_id']
        first_message = self.order_info[order_id]
        symbol = first_message['symbol']
  
        if message['type'] == 'CANCEL_ACK':
            self.process_cancel_ack(order_id,symbol)
            
        if message['type'] == 'ORDER_REJECT':
            "increase the position in sales order"
            self.process_order_reject(order_id,symbol)
             
        if message['type'] == 'ORDER_ACCEPT':
            "Increase the position in buy order"
            self.process_order_accept(order_id,symbol)
            
        if message['type'] == 'FILL':
            filled_quantity = message['filled_quantity']
            self.process_fill(order_id,symbol,filled_quantity)
            
        
        return self.marking_position[symbol]
        
    def process_new(self,message):
        self.order_info[message['order_id']] = message
        
        if  message['symbol'] not in self.marking_position:
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
            
    def process_order_accept(self,order_id,symbol):
        #order = self.order_info[message['order_id']]
        #if order['side'] is 'BUY':
            #self.marking_position[order['symbol']] += order['quantity']
        pass
        
    def process_fill(self,order_id,symbol,filled_quantity):
        order = self.order_info[order_id]
        
        if order['side'] == 'BUY':
            self.marking_position[symbol] += filled_quantity


if __name__== '__main__':
    m = MarkingPositionMonitor()
    with open(sys.argv[1],'r') as fd:
        for line in fd:
            print(m.on_event(line))
