class Stack:
    
    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        return not self.stack
                
    # empilha elementos    
    def push(self, item):
        self.stack.append(item)
        
    # desempilha elementos     
    def pop(self):
        if self.is_empty():
            print('A pilha está vazia')
            return None
        else:
            return self.stack.pop()
            
    def top(self):
        if self.is_empty():
            return None
        else: 
            return self.stack[-1]            

    def is_valid_sequence(self, initial_sequence, target_sequence):
        index = 0 
        for elemento in target_sequence:
            while self.is_empty() or self.top() != elemento:
                if index >= len(initial_sequence):
                    return False
                self.push(initial_sequence[index])
                index += 1
            if self.top() == elemento:
                self.pop()    
        return self.is_empty()
        
stack = Stack()
initial_sequence = [1, 2, 3, 4, 5]
target_sequence = [5, 4, 3, 2, 1]

resultado = stack.is_valid_sequence(initial_sequence, target_sequence)
print(resultado)  
